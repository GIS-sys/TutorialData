from creator import Creator
import random
import time


# Names, dates, cities

def random_datetime(start="2010-01-01 00:00:00", end="2020-12-31 23:59:59", time_format="%Y-%m-%d %H:%M:%S"):
    prop = random.random()
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

M = 16
NAMES_F = ["Маша", "Ангелина", "Саша", "Яна", "Лиза", "Мора", "Эмми", "Белла", "Василисса", "Настя", "Оля", "Ира", "Чарли", "Кармилла", "Любовь", "Вера"]
NAMES_M = ["Гордей", "Эрнест", "Саша", "Ян", "Лерой", "Морти", "Этан", "Бернард", "Василий", "Натан", "Аркадий", "Илон", "Аластор", "Энджел Даст", "Валентин", "Вокс"]
CITIES = ["Москва", "Санкт-Петербург", "Обнинск", "Новосибирск", "Лас-Вегас", "Лос-Анджелес", "Нью-Йорк", "Вашингтон", "Ватикан", "Осло", "Томск", "Долгопрудный", "Пермь", "Орёл", "Париж", "Лондон"]
WEIGHTS = [M-i for i in range(M)]
DATES = [random_datetime() for i in range(M)]

N = 1000
data = [["Муж", "Муж (город рождения)", "Жена", "Жена (город рождения)", "Дата путешествия"]] + [
    [
        random.choices(NAMES_M, weights=WEIGHTS)[0],
        random.choices(CITIES, weights=WEIGHTS)[0],
        random.choices(NAMES_F, weights=WEIGHTS)[0],
        random.choices(CITIES, weights=WEIGHTS)[0],
        random.choices(DATES, weights=WEIGHTS)[0]
    ] for i in range(N)
]
data = data[:1] + [[NAMES_M[0], CITIES[0], NAMES_F[0], CITIES[1], DATES[0]]] + data[1:]
Creator.xlsx(data, "data/data_random_nonnumbers.xlsx")
