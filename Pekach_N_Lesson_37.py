# Lesson 37
# Task 1

import socket
import threading
from collections import deque


# сервер чата (TCP, потоки, очередь сообщений)
class ChatServer:
    def __init__(self, host='127.0.0.1', port=5555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.messages = deque(maxlen=100)  # Очередь последних 100 сообщений

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message.encode('utf-8'))
            except:
                self.clients.remove(client)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.messages.append(message)
                self.broadcast(message)
            except:
                self.clients.remove(client)
                break

    def start(self):
        print("Сервер запущен!")
        while True:
            client, addr = self.server.accept()
            print(f"Подключен {addr}")
            self.clients.append(client)
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()


# клиент чата
class ChatClient:
    def __init__(self, host='127.0.0.1', port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                print(message)
            except:
                print("Ошибка!")
                self.client.close()
                break

    def send(self):
        while True:
            message = input()
            self.client.send(message.encode('utf-8'))

    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()


# Запуск
if __name__ == "__main__":
    choice = input("Запустить сервер (s) или клиент (c)? ")
    if choice == "s":
        server = ChatServer()
        server.start()
    elif choice == "c":
        client = ChatClient()
        client.start()


'''
Запустите сервер: python chat.py → введите 's'

Запустите клиенты в других окнах: python chat.py → введите 'c'

Ввeдите сообщения в клиентах - появятся у всех
'''