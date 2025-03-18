# Lesson 31

'''UDP Client'''
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 12345)

while True:
    message = input("Введите сообщение для сервера: ")
    client_socket.sendto(message.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print(f"Ответ сервера: {data.decode()}")
