import socket

serverAddressPort   = ("192.168.1.28", 6000)

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
bytesToSend = input("> ")
UDPClientSocket.sendto(str.encode(bytesToSend), serverAddressPort)