import socket
#socket.AF_INET :ipv4
#socket.SOCK_DGRAM :UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("hello world !",("30.9.75.120",5005))
s.close()