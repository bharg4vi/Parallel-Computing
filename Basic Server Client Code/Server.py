import socket

PORT = 8080
hello = "Hello from server Bhargavi Kamble"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(3)
client_socket, client_address = server_socket.accept()
data = client_socket.recv(1024).decode()
print(data)
client_socket.send(hello.encode())
client_socket.close()
server_socket.close()
