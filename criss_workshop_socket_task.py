import socket

serverIP = '172.17.29.11'
serverPORT = 6000

serveraddress = (serverIP, serverPORT)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = 'Hi, My name is '
bytestosend = str.encode(message)
UDPClientSocket.sendto(bytestosend, serveraddress)

