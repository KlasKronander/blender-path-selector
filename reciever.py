import socket
import time
import json


IP = 'localhost'
port = 5005
addr = (IP,port)
buf = 4*4096

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)

while True:
    data,addr = s.recvfrom(buf)
    if data:
        vertice_coordinates = json.loads(data.decode("utf-8"))
        print vertice_coordinates


