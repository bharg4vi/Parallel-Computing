import socket

PORT = 8080
hello = "Hello from client 202051048"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', PORT))

client_socket.send(hello.encode())
buffer = client_socket.recv(1024).decode()
print(buffer)

client_socket.close()
