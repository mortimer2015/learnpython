import socket
import json

sock = socket.socket()
sock.bind(('127.0.0.1', 4001))
sock.listen()
so, addr = sock.accept()
data = so.recv(1024)
print(json.loads(data.decode()))