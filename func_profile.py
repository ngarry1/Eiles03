#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 22.08.2020
import cProfile
from typing import List

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


cProfile.run('task004(1000)')


