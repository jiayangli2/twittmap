import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname();
port=8091;
s.bind((host, port))
s.listen(5)
clientSocket, clientAddr = s.accept()

while True:
    msg = clientSocket.recv(4096)    
    start=msg.find('\n  "Message"')
    start +=16
    mtemp=msg[start:]
    end = mtemp.find('",\n')
    rmsg = mtemp[0:end]
    print rmsg
