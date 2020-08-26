#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 23.06.2020
from typing import List
import math
import pytest


@pytest.mark.skip(reason='Проверено')
def test_task01():
    """ Тест задачи 001"""

    task001_const: list = [10, 3, 5]
    number_sum: int = 0

    for num in range(3, task001_const[0]):
        if (num % task001_const[1] == 0) or (num % task001_const[2] == 0):
            number_sum += num
    assert number_sum == 23


@pytest.mark.skip(reason='Проверено')
def test_task02():
    """ Тест задачи 002"""

    const_task: int = 10

    def fibonacci(n: int) -> int:
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    def fib_sum() -> int:
        fib_sum_even: int = 0
        current_fib_number: int = 0

        while current_fib_number <= const_task:
            current_fib_number += 1
            fib_number = fibonacci(current_fib_number)
            if (fib_number % 2) == 0:
                fib_sum_even += fib_number
        return fib_sum_even

    assert fib_sum() == 44


@pytest.mark.skip(reason='Проверено')
def test_task003():
    """Задача 003"""

    answer: list = []
    divider: int = 2
    const_task = 13195

    while divider * divider <= const_task:
        if const_task % divider == 0:
            answer.append(divider)
            const_task //= divider
        else:
            divider += 1
    if const_task > 1:
        answer.append(const_task)

# Проверка списка answer
    assert len(answer) == 4
    assert answer[0] == 5
    assert answer[1] == 7
    assert answer[2] == 13
    assert answer[3] == 29

    return answer


@pytest.mark.skip(reason='Проверено')
def test_task006():
    """ Тест задачи 006"""

    task006_const: int = 10
    number10s: List[int] = [j ** 2 for j in range(1, task006_const + 1)]
    number10_sum_s: List[int] = [j for j in range(1, task006_const + 1)]
    difference: int = sum(number10_sum_s) ** 2 - sum(number10s)
    assert sum(number10s) == 385
    assert sum(number10_sum_s) ** 2 == 3025
    assert difference == 2640

    return difference


def test_task007():
    """ Тест задачи 007"""

    test_list: List[int] = [2, 3, 5, 7, 11, 13]
    count: int = 6

    number: int = 13
    lst: List[int] = []
    k: int = 0
    while k <= count:
        for i in range(2, count + 1):
            if i > 10:
                if (i % 2 == 0) or (i % 10 == 5):
                    continue
            for j in lst:
                if j > int((math.sqrt(i)) + 1):
                    lst.append(i)
                    break
                if i % j == 0:
                    break
            else:
                lst.append(i)
        k = k + 1

    # assert test_list == lst
    # assert count == len(test_list)

    return lst
