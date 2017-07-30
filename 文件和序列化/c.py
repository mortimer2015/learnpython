import socket
import json
data = {a: 1, b: 2}
so = socket.socket()
so.connect(('127.0.0.1', 4001))
so.send(json.dumps(data).encode())