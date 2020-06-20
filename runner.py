#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020

# from typing import List


def print_task() -> None:
    QUESTION: str = 'Если выписать все натуральные числа меньше 10, кратные 3 или 5,\
     то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.'
    ANSWER: str = 'Найдите сумму всех чисел меньше 1000, кратных 3 или 5.'
    # print('Привет!')
    TASK_CONST: list = [1000, 3, 5]
#    print('Task const', TASK_CONST)
    print(QUESTION)
    print(ANSWER)


def task01() -> int:
    result: int = 0
    print_task()
    return result


if __name__ == '__main__':
    print('Результат: ', str(task01()))


