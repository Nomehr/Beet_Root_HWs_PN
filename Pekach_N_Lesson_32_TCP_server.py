# Lesson 31
'''TCP server'''

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)

print("Сервер запущен и ожидает подключения...")

conn, addr = server_socket.accept()
print(f"Клиент {addr} подключился")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Получено от клиента: {data.decode()}")
    conn.sendall(f"Принято: {data.decode()}".encode())

conn.close()
server_socket.close()
