# Lesson 31

'''Extended UDP Client'''
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Введите сообщение: ")
    shift = input("Введите ключ (сдвиг): ")

    if message.lower() == "exit":
        break

    client_socket.sendto(f"{message}:{shift}".encode(), ("127.0.0.1", 12345))
    response, _ = client_socket.recvfrom(1024)
    print(f"Зашифрованное сообщение от сервера: {response.decode()}")

client_socket.close()