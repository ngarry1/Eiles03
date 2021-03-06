#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020

from typing import Tuple, List
from functions import prime


def task001(const_task: Tuple) -> int:
    """Задача 001

    Если выписать все натуральные числа меньше 10,
    кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """

    # task001_const: Tuple[int, int, int] = (10, 3, 5)

    number_sum: int = 0
    for num in range(3, const_task[0]):
        if (num % const_task[1] == 0) or (num % const_task[2] == 0):
            number_sum += num
    return number_sum


def task002(const_task: int) -> int:
    """Задача 002

    Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
    Начиная с 1 и 2, первые 10 элементов будут:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
    """

    def fibonacci(n_f: int) -> int:
        if n_f in (1, 2):
            return 1
        return fibonacci(n_f - 1) + fibonacci(n_f - 2)

    def fib_sum() -> int:
        fib_sum_even: int = 0
        current_fib_number: int = 1

        while fib_sum_even < const_task:
            fib_number = fibonacci(current_fib_number)
            if (fib_number % 2) == 0:
                fib_sum_even += fib_number
            current_fib_number += 1
        return fib_sum_even

    return fib_sum()


def task003(const_task: int) -> list:
    """Задача 003

    Простые делители числа 13195 - это 5, 7, 13 и 29.

    Каков самый большой делитель числа 600851475143, являющийся простым числом?
    """

    answer: list = []
    divider: int = 2

    while divider * divider <= const_task:
        if const_task % divider == 0:
            answer.append(divider)
            const_task //= divider
        else:
            divider += 1
    if const_task > 1:
        answer.append(const_task)

    return answer


def task004(task004_const) -> int:
    """Задача 004

    Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
    Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

    Найдите самый большой палиндром, полученный умножением двух трехзначных чисел."""

    polyndrome_list_result: List[int] = []

    for divider_item1 in range(10, task004_const):
        for divider_item2 in range(divider_item1, task004_const):
            multiply = divider_item1 * divider_item2
            if str(multiply) == str(multiply)[::-1]:
                # multiply = max()
                polyndrome_list_result.append(multiply)
    return max(polyndrome_list_result)


# def task005(task005_const) -> int:
#     """Задача 005
#
#     2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
#     Какое самое маленькое число делится нацело на все числа от 1 до 20? """


def task006(task006_const) -> int:
    """Задача 006
    Сумма квадратов первых десяти натуральных чисел равна:
    1^2 + 2^2 + ... + 10^2 = 385
    Квадрат суммы первых десяти натуральных чисел равен:
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел
    составляет 3025 − 385 = 2640.

    Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел."""

    number10s: List[int] = [j ** 2 for j in range(1, task006_const + 1)]
    number10_sum_s: List[int] = [j for j in range(1, task006_const + 1)]

    return sum(number10_sum_s) ** 2 - sum(number10s)


def task007(task007_const):
    """Задача 007
        Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
        Очевидно, что 6-ое простое число - 13.

        Какое число является 10001-ым простым числом?"""

    number_natural: int = 2
    while len(prime(number_natural)) < task007_const:
        number_natural += 1

    return prime(number_natural)[-1]

