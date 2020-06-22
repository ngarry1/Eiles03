#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020

from typing import Tuple

# Задача 001
question: str = 'Задача номер 001: \n' + 'Если выписать все натуральные числа меньше 10,\
 кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.'
answer: str = 'Найдите сумму всех чисел меньше 1000, кратных 3 или 5.\n'
task001_const: Tuple[int, int, int] = (10, 3, 5)


def task001(q: str, ans: str) -> None:
    """Вывод на печать задачи 001"""

    print(q, ans)


task001(question, answer)


def task01() -> int:
    """Решение задачи 001"""

    number_sum: int = 0
    for num in range(3, task001_const[0]):
        if (num % task001_const[1] == 0) or (num % task001_const[2] == 0):
            number_sum += num
    return number_sum
