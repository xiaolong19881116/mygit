import socket
#socket.AF_INET :ipv4
#socket.SOCK_DGRAM :UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",5005)) # "" <-->self 
data,addr = s.recvfrom(1024) # buffer 1024B 
print "received message :%s" % data
print "from :",addr
s.close() 
