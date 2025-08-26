# UDP Network Library
#
# filcher, 2025 (C)

import socket
import json

fullpath = ()
client_socket = ''

def initilitaion(host):
    global fullpath, client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fullpath = host

def sendCoordinate(x: int, y: int, z: int) -> json:
    coordinate = {
        "x": x,
        "y": y,
        "z": z
    }
    cjson = json.dumps(coordinate)
    client_socket.sendto(cjson.encode('utf-8'), fullpath)

def sendCoordinateAndMessage(x: int, y: int, z: int, message: str) -> json:
    coordinate = {
        "x": x,
        "y": y,
        "z": z,
        "comment": message
    }
    cjson = json.dumps(coordinate)
    client_socket.sendto(cjson.encode('utf-8'), fullpath)

def info() -> str:
    print("UPD NETWORK LIBRARY FROM OLIMP")
    print("Author: filcher")

def hostInfo() -> str:
    global fullpath
    ipI, portI = fullpath
    print(f"Connection on {ipI}:{portI}")