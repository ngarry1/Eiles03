#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 23.06.2020
# from typing import Tuple
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
