from creator import Creator
import random


# Names, dates, cities

def random_datetime():
    return ""

NAMES_F = ["Маша", "Ангелина", "Саша", "Яна", "Лиза", "Мора", "Эмми", "Белла", "Василисса", "Настя", "Оля", "Ира", "Чарли", "Кармилла", "Любовь", "Вера"]
NAMES_M = ["Гордей", "Эрнест", "Саша", "Ян", "Лерой", "Морти", "Этан", "Бернард", "Василий", "Натан", "Аркадий", "Илон", "Аластор", "Энджел Даст", "Валентин", "Вокс"]
CITIES = ["Москва", "Санкт-Петербург", "Обнинск", "Новосибирск", "", "", "", "", "", "", "", "", "", "Вашингтон", "Париж", "Лондон"]
DATES = [random_datetime() for i in range(16)]

N = 1000
data = [["Муж", "Муж (город рождения)", "Жена", "Жена (город рождения)", "Дата путешествия"]] + [
    [random.choice(NAMES_M), random.choice(CITIES), random.choice(NAMES_F), random.choice(CITIES), random.choice(DATES)] for i in range(N)
]
data = data[:2] + [NAMES_M[0], NAMES_F[0], CITIES[0], DATES[0]]
Creator.xlsx(data, "data/data_random_nonnumbers.xlsx")
