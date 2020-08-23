#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 23.06.2020
"""Измерение производительности"""

from typing import List, Tuple
from timeit import default_timer as timer


def measure_time(func):
    """Декоратор измерения"""

    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'Функция {func.__name__} выполняется {end - start} секунд')

    return inner


@measure_time
def task001(const_task: Tuple) -> int:
    """Задача 001

    Если выписать все натуральные числа меньше 10,
    кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """

    number_sum: int = 0
    for num in range(3, const_task[0]):
        if (num % const_task[1] == 0) or (num % const_task[2] == 0):
            number_sum += num
    return number_sum


# task001((1000, 3, 5))  # Вызов задачи 001
# -------------------------------------------------------------------------------------------


@measure_time
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


# task002(4000000) # Вызов задачи 002
# -------------------------------------------------------------------------------------------
@measure_time
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


# task003(600851475143)
# -------------------------------------------------------------------------------------------
@measure_time
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
                polyndrome_list_result.append(multiply)
    return max(polyndrome_list_result)


task004(1000)
# -------------------------------------------------------------------------------------------
