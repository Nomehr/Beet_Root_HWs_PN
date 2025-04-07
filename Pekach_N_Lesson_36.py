# Lesson 36
# Task 1

import asyncio
import time
from multiprocessing import Pool


# Асинхронные функции
async def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


async def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


async def square(n):
    return n * n


async def cube(n):
    return n * n * n


# Мультипроцессинг функции
def fib_sync(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fact_sync(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def square_sync(n):
    return n * n


def cube_sync(n):
    return n * n * n


async def async_main():
    numbers = list(range(1, 11))
    tasks = []

    for n in numbers:
        tasks.append(fib(n))
        tasks.append(fact(n))
        tasks.append(square(n))
        tasks.append(cube(n))

    results = await asyncio.gather(*tasks)

    # Разделяем результаты по функциям
    fibs = results[::4]
    facts = results[1::4]
    squares = results[2::4]
    cubes = results[3::4]

    print("Async results:")
    print("Fibonacci:", fibs)
    print("Factorials:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)


def sync_main():
    numbers = list(range(1, 11))
    with Pool() as pool:
        fibs = pool.map(fib_sync, numbers)
        facts = pool.map(fact_sync, numbers)
        squares = pool.map(square_sync, numbers)
        cubes = pool.map(cube_sync, numbers)

    print("\nMultiprocessing results:")
    print("Fibonacci:", fibs)
    print("Factorials:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(async_main())
    print(f"Async time: {time.time() - start:.4f} sec")

    start = time.time()
    sync_main()
    print(f"Multiprocessing time: {time.time() - start:.4f} sec")

'''
Asyncio vs Multiprocessing:

I/O (сеть, файлы) → Asyncio (легковесный, 1 поток)
CPU (вычисления) → Multiprocessing (истинный параллелизм)

Ждёшь ответа? → Asyncio
Считаешь? → Multiprocessing

Asyncio для ожидания, Multiprocessing для вычислений.
'''

# Task 2

import aiohttp
import asyncio
import json

from datetime import datetime


async def fetch_comments(session, subreddit, size=1000):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size={size}"
    try:
        async with session.get(url) as response:
            return await response.json()
    except Exception as e:
        print(f"Error: {e}")
        return {'data': []}


async def main():
    subreddit = "python"
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_comments(session, subreddit) for _ in range(5)]
        results = await asyncio.gather(*tasks)

        comments = []
        for result in results:
            comments.extend(result['data'])

        # Сортируем по дате
        comments.sort(key=lambda x: x['created_utc'])

        with open(f"{subreddit}_async_comments.json", 'w') as f:
            json.dump(comments, f, indent=2)

        print(f"Saved {len(comments)} comments")


if __name__ == "__main__":
    asyncio.run(main())

# Task 3

import asyncio


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected: {addr}")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            writer.write(data)
            await writer.drain()
    except ConnectionError:
        pass
    finally:
        writer.close()
        print(f"Disconnected: {addr}")


async def main():
    server = await asyncio.start_server(
        handle_client,
        'localhost',
        65432
    )
    print("Server started on localhost:65432")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())