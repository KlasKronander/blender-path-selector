import socket
import time

IP = 'localhost'
port = 5005
addr = (IP,port)
buf = 4096

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)
while True:
    data,addr = s.recvfrom(buf)
    if data:
        print data
        print "end of message"
    
