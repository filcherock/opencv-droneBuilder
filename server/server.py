import socket
import sys
import os

from colorama import *
#import keyboard

init()

host = input(f"Please, enter IP for connect: {Fore.GREEN}")
#"192.168.39.119"
port = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input(f"{Fore.RESET}>> ")
    client_socket.sendto(message.encode('utf-8'), (host, port))
    print(f"Отправлено: {Fore.GREEN}{message}{Fore.RESET}")

    data, addr = client_socket.recvfrom(1024)
    print(f"Получен ответ от {addr}: {data.decode('utf-8')}")

    a = input("Press any key to send new message (q - exit, cls - clear console and new message)")
    if a == "q":
        client_socket.close()
        sys.exit()
    elif a == "cls":
        os.system('cls')
    else:
        pass