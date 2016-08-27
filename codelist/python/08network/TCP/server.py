import socket 
HOST = ''            #server IP 
PORT = 50007         #server port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
print "listen as port:",PORT 
conn,addr = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break 
    conn.sendall("from server:"+data)
conn.close()