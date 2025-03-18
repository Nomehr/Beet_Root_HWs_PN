# Lesson 31

'''Extended UDP Server'''
import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))

print("UDP сервер запущен и ожидает сообщений...")

while True:
    data, addr = server_socket.recvfrom(1024)
    try:
        message, shift = data.decode().rsplit(":", 1)
        shift = int(shift)
        encrypted_message = caesar_cipher(message, shift)
        server_socket.sendto(encrypted_message.encode(), addr)
    except ValueError:
        server_socket.sendto("Ошибка: неверный формат данных!".encode(), addr)
