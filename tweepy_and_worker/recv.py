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
