# Lesson 31
'''TCP client'''

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

while True:
    message = input("Введите сообщение для сервера: ")
    if message.lower() == "exit":
        break
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024)
    print(f"Ответ сервера: {response.decode()}")

client_socket.close()
