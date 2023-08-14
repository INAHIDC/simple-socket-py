import socket 


HOST = " "
PORT = 9090

socket = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hola".encode('utf-8'))
print(socket.recv(1024))
