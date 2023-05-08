import socket

HOST = '192.168.21.130'  # put the IP address of the server here
PORT = 5000  # choose the same port number as the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    while True :
        data = s.recv(1024)
        print('Received', repr(data))
