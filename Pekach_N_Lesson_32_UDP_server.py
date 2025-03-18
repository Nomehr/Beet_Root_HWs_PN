# Lesson 31

'''UDP Server'''
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))

print("UDP сервер запущен и ожидает данных...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Получено сообщение от {addr}: {data.decode()}")
    response = f"Принято: {data.decode()}"
    server_socket.sendto(response.encode(), addr)