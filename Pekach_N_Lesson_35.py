# Lesson 35
# Task 1

import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def run_with_executor(executor_class, numbers):
    """Запускает проверку чисел с использованием executor"""
    with executor_class() as executor:
        results = list(executor.map(is_prime, numbers))
    return results


def main():
    # Проверяем все реализации
    for name, executor in [("Threads", ThreadPoolExecutor),
                           ("Processes", ProcessPoolExecutor)]:
        start = time.time()
        results = run_with_executor(executor, NUMBERS)
        elapsed = time.time() - start

        print(f"\n{name} results:")
        for num, res in zip(NUMBERS, results):
            print(f"{num} is prime: {res}")
        print(f"Time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()

'''
ProcessPool (процессы)
    Лучше для тяжелых вычислений (CPU-bound)
    Минус: больше расходов памяти

ThreadPool (потоки)
    Лучше для операций ввода-вывода (I/O-bound)
    Минус: есть GIL (не для вычислений)

Если задача "считает" → процессы
Если задача "ждет" (сеть/диск) → потоки
'''

# Task 2

import requests
import json
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime


def fetch_comments(subreddit, size=1000):
    """Загружает комментарии с Reddit API"""
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size={size}"
    try:
        response = requests.get(url, timeout=10)
        return response.json()['data']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []


def save_to_file(comments, filename):
    """Сохраняет комментарии в JSON файл"""
    sorted_comments = sorted(comments, key=lambda x: x['created_utc'])
    with open(filename, 'w') as f:
        json.dump(sorted_comments, f, indent=2)


def run_concurrent(subreddit, executor_class, filename):
    """Запускает загрузку с использованием concurrent"""
    with executor_class(max_workers=5) as executor:
        futures = [executor.submit(fetch_comments, subreddit) for _ in range(5)]
        comments = []
        for future in futures:
            comments.extend(future.result())

    save_to_file(comments, filename)
    print(f"Saved {len(comments)} comments to {filename}")


if __name__ == "__main__":
    subreddit = "python"

    # Запуск с ThreadPoolExecutor
    run_concurrent(subreddit, ThreadPoolExecutor, "comments_threads.json")

    # Запуск с ProcessPoolExecutor
    run_concurrent(subreddit, ProcessPoolExecutor, "comments_processes.json")

# Task 3

import socket
from multiprocessing import Process


def handle_client(conn, addr):
    """Обрабатывает соединение с клиентом"""
    print(f"Connected: {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    finally:
        conn.close()
    print(f"Disconnected: {addr}")


def start_server(host='localhost', port=65432):
    """Запускает сервер"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"Server started on {host}:{port}")

        while True:
            conn, addr = s.accept()
            p = Process(target=handle_client, args=(conn, addr))
            p.start()
            conn.close()  # Закрываем копию сокета в родительском процессе


if __name__ == "__main__":
    start_server()