import socket 
HOST = '127.0.0.1'   #server IP 
PORT = 50007         #server port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall(b"hello world!")
data = s.recv(1024)
s.close()
print data