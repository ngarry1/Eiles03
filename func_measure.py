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
    """Задача 001"""

    number_sum: int = 0
    for num in range(3, const_task[0]):
        if (num % const_task[1] == 0) or (num % const_task[2] == 0):
            number_sum += num
    return number_sum


# task001((1000, 3, 5))  # Вызов задачи 001
# -------------------------------------------------------------------------------------------


@measure_time
def task002(const_task: int) -> int:
    """Задача 002"""

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
    """Задача 003"""

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
    """Задача 004"""

    polyndrome_list_result: List[int] = []

    for divider_item1 in range(10, task004_const):
        for divider_item2 in range(divider_item1, task004_const):
            multiply = divider_item1 * divider_item2
            if str(multiply) == str(multiply)[::-1]:
                polyndrome_list_result.append(multiply)
    return max(polyndrome_list_result)


# task004(1000)
# -------------------------------------------------------------------------------------------
@measure_time
def task006(task006_const) -> int:
    """Задача 006"""

    number10s: List[int] = [j ** 2 for j in range(1, task006_const + 1)]
    number10_sum_s: List[int] = [j for j in range(1, task006_const + 1)]

    return sum(number10_sum_s) ** 2 - sum(number10s)


# task006(100)

# -------------------------------------------------------------------------------------------
