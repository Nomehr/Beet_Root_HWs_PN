# Lesson 35
# Task 1

import threading

counter = 0
rounds = 100000
lock = threading.Lock()

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            lock.acquire()
            try:
                counter += 1
            finally:
                lock.release()

# Потоки
t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Ожидаемое значение: {2 * rounds}")
print(f"Фактическое значение: {counter}")

# Task 2

import socket
import threading


def handle_client(conn, addr):
    print(f"Подключен клиент {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)  # возврат данных
    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 87654))
    server.listen()
    print("Сервер запущен.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()

# Task 3

import requests
import threading
import json
from datetime import datetime

comments = []
lock = threading.Lock()


def fetch_comments(subreddit, size=1000):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size={size}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with lock:
                comments.extend(response.json()['data'])
    except Exception as e:
        print(f"Ошибка: {e}")


def save_comments(subreddit):
    # Сортируем по дате
    sorted_comments = sorted(comments, key=lambda x: x['created_utc'])

    with open(f"{subreddit}_comments.json", 'w') as f:
        json.dump(sorted_comments, f, indent=4)


if __name__ == "__main__":
    subreddit = "python"
    threads = []

    # 5 потоков параллельных запросов
    for _ in range(5):
        t = threading.Thread(target=fetch_comments, args=(subreddit,))
        t.start()
        threads.append(t)

    # Завершение потоков
    for t in threads:
        t.join()

    # Результат
    save_comments(subreddit)
    print(f"Сохранено {len(comments)} комментариев в {subreddit}_comments.json")