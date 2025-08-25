import socket
import time

class ConveyerLine():
    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def setSpeed(self,s):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        self.UDPClientSocket.sendto(str.encode(f"s:{s}#"), self.serverAddressPort)

class ConveyerMuver():
    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def setPosition(self,point):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        self.UDPClientSocket.sendto(str.encode(f"s:1:{point}#"), self.serverAddressPort)

class ConveyerLineNamet():
    def __init__(self, ip:str, port:int, name:str) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)
        self.name=name

    def setSpeed(self,s):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        self.UDPClientSocket.sendto(str.encode(f"{self.name}:{s}#"), self.serverAddressPort)
        time.sleep(0.5)

class Manipulator():
    def __init__(self, ip:str, port:int, type:str) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.type=type
        self.serverAddressPort = (ip, port)


    def toPoint(self,x, y, z, a=0, g=0):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        if self.type=="g":
            self.UDPClientSocket.sendto(str.encode(f"{self.type}:{x}:{y}:{a}:{z}:{g}#"), self.serverAddressPort)
        if self.type=="p":
            self.UDPClientSocket.sendto(str.encode(f"{self.type}:{x}:{y}:{z}:{g}#"), self.serverAddressPort)
class Lamp():

    def __init__(self, ip:str, port:int) -> None:
        self.ip=ip
        self.port=port
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.serverAddressPort = (ip, port)


    def setColor(self,r=0,g=0,b=0,y=0):
        msgFromClient=f"l:{r}:{b}:{g}:{y}#"
        print(msgFromClient)
        bytesToSend = str.encode(msgFromClient)
        bufferSize = 1024
        self.UDPClientSocket.sendto(bytesToSend, self.serverAddressPort)