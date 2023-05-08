import socket
import time

HOST = '192.168.21.130'  # put the IP address of the server here
PORT = 5001  # choose a port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        #with conn:
        while True:
            print('Connected by', addr)
            while True:
                #data = conn.recv(1024)
                data= b'amit'
                print(str(data)[1:])
                #if not data:
                #   break
                time.sleep(2)
                conn.sendall(data)


