import socket
import time

IP = 'localhost'
port = 5005
addr = (IP,port)
buf = 4096

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    s.sendto("hejsan",addr)
    print "sent a message"
    time.sleep(3)
    
