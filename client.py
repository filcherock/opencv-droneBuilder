import socket
import os
import json
import datetime

from colorama import *

init()

def main():
    try:
        host, port = input(f"{Fore.RESET}ip:host >> {Fore.GREEN}").split(":")

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((host, int(port)))

        print(f"{Fore.CYAN}The client started listening to the address {host}:{port}{Fore.RESET}")

        while True:
            data, addr = server_socket.recvfrom(1024)
            msg = {
                "ipServer": addr,
                "message": data.decode('utf-8'),
                "datetime": str(datetime.datetime.now().strftime("%D | %H:%M:%S"))
            }
            print("=========================================================")
            print("  New message!")
            print(f"  Sender: {msg['ipServer']}")
            print(f"  Message: {msg['message']}")
            print(f"  Date & Time: {msg['datetime']}")
            print("=========================================================")
            with open('log.txt', "w") as file:
                file.write(f"[{msg['datetime']}] {msg['ipServer']} =: {msg['message']}")
                file.close()

            response = json.dumps(msg)
            server_socket.sendto(response.encode('utf-8'), addr)
    except ValueError:
        print(f"{Fore.RED}The value you entered is incorrect!{Fore.RESET}")
        main()
    except OSError as e:
        print(f"{Fore.RED}A server error occurred: {e}{Fore.RESET}")

if __name__ == '__main__':
    main()
