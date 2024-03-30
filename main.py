from creator import Creator
from decimal import Decimal, getcontext
from math import factorial, pi, sin
import random


def nth_pi_digit(n):
    n += 2
    getcontext().prec=n+1
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k=0
    t=(1)*(factorial(1))*(13591409+545140134*k)
    deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
    pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return str(pi)[-2]


N = 1000
data = [["Броски кубика", "Броски монетки", "Синус случайного аргумента", "Цифры числа PI"]] + [
    [random.randint(1, 6), random.randint(0, 1), sin(random.random() * 2 * pi), nth_pi_digit(i)] for i in range(N)
]
Creator.csv(data, "data/data_random_numbers.csv")


#Creator.xlsx(data, "data/simple_random.xlsx")
