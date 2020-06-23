#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020

from typing import Tuple


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
