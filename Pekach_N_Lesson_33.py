# Lesson 33
## Task 1 Robots.txt

import requests

# Список сайтов
websites = [
    "https://en.wikipedia.org/robots.txt",
    "https://twitter.com/robots.txt"
]

# Скачиваем и сохраняем robots.txt
for url in websites:
    response = requests.get(url)
    if response.status_code == 200:
        domain = url.split("//")[1].split("/")[0]  # Извлекаем доменное имя
        with open(f"{domain}_robots.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Файл {domain}_robots.txt успешно сохранен.")
    else:
        print(f"Ошибка при загрузке {url}: {response.status_code}")

## Task 2 Reddit

import requests
import json

# Параметры запроса
subreddit = "python"  # Выберите сабреддит
url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size=1000"

# Отправляем запрос
response = requests.get(url)
if response.status_code == 200:
    comments = response.json()["data"]

    # Сортируем комментарии по дате (хронологический порядок)
    comments_sorted = sorted(comments, key=lambda x: x["created_utc"])

    # Сохраняем в JSON
    with open(f"{subreddit}_comments.json", "w", encoding="utf-8") as file:
        json.dump(comments_sorted, file, indent=4)
    print(f"Комментарии сохранены в {subreddit}_comments.json.")
else:
    print(f"Ошибка при загрузке комментариев: {response.status_code}")

## Task 3 Wether

import requests

# API-ключ OpenWeatherMap
API_KEY = "e7ac81329c1f5e87a2de8f3e78d1d035"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    # Параметры запроса
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Для получения температуры в градусах Цельсия
        "lang": "ua"  # Для получения данных на украинском языке
    }

    # Отправляем запрос
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()

        # Извлекаем данные
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Выводим результат
        print(f"Погода в городе {city}:")
        print(f"Описание: {weather}")
        print(f"Температура: {temp}°C")
        print(f"Влажность: {humidity}%")
        print(f"Скорость ветра: {wind_speed} м/с")
    else:
        print(f"Ошибка: {response.status_code}. Проверьте название города или API-ключ.")


if __name__ == "__main__":
    city = input("Введите название города: ")
    get_weather(city)