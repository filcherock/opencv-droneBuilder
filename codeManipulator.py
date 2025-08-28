import socket
import json
from socket import fromfd
import promtools
from promtools import ConveyerLineNamet, Manipulator
import threading
import  time

M =promtools.Manipulator("192.168.10.16", 8888, "g")
C =promtools.ConveyerLineNamet("192.168.10.21", 8888, "B")

def poluch(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"Слушаю {ip}:{port}...")

    try:
        # Шаг 1: Ждём сообщение "ready"
        print("Ожидаю 'ready'...")
        while True:
            data, addr = sock.recvfrom(1024)
            if not data:
                continue  # Пропускаем пустые пакеты
            message = data.decode('utf-8')
            print(f"Получено: {message}")
            dictResult = json.loads(message)
            dictResult1 = dictResult.get("status")

            if dictResult1 == "ready":
                print("Получено 'ready'")
                M.toPoint(100, 0, 180, 200, 1)
                M.toPoint(200, 0, 100, 199, 0)
                break

        # Шаг 2: После 'ready' ждём JSON
        print("Ожидаю JSON с данными...")
        data, addr = sock.recvfrom(1024)
        if not data:
            print("Получены пустые данные после 'ready'.")
            return None

        message = data.decode('utf-8')
        print(f"Получен JSON: {message}")

        dictResult = json.loads(message)
        x1 = int(dictResult.get("x"))
        y1 = dictResult.get("y")

        print(f"Распарсено: x={x1}, y={y1}")
        return {"x": x1, "y": y1}

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        sock.close()

# === Основной код ===
result = poluch('0.0.0.0', 8888)

if result is not None:
    x2 = result["x"]
    y2 = result["y"]

else:
    print("Не удалось получить данные.")
M.toPoint(x2, y2 ,200, 100, 1)
M.toPoint(200, 0, 180, 198, 0)
if M.toPoint(200, 0, 180, 198, 0):
        C.setSpeed(100)
        time.sleep(5)
        C.setSpeed(0)
