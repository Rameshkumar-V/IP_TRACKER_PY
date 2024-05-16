import socket
from pickle import  dumps

IP = '127.2.0.2'  # Specify the IP address of the server
PORT = 6000     # Specify the port number of the server

client_socket = socket.socket()

client_socket.bind((IP, PORT))
client_socket.listen(1)

print('Client is listening...')

# Accept incoming connection from the server
server_socket, server_address = client_socket.accept()
print(f"Connection from {server_address} has been established.")

received_message = server_socket.recv(1024)
if received_message==b"Are you on?":
    server_socket.sendall(dumps('True'))
else:
    server_socket.sendall(dumps('False'))


print("Message from server:", received_message.decode())

# Close the connection
server_socket.close()
