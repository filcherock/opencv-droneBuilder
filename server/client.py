import socket

from colorama import *

init()

host = '192.168.39.176'
port = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"{Fore.CYAN}Сервер слушает на {host}:{port}{Fore.RESET}")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Получено от {addr}: {Fore.GREEN}{data.decode('utf-8')}{Fore.RESET}")

    response = f"Сервер получил: {data.decode('utf-8')}"
    server_socket.sendto(response.encode('utf-8'), addr)