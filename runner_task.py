#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020
"""Точка входа в проект"""

# import collections
import tasks
from typing import Tuple  # Для задачи 001

# task001_const: Tuple[int, int, int] = (10, 3, 5) # Для задачи 001
# task002_const: int = 4000000
# task003_const: int = 600851475143
# task003_const: int = 2

params = {
    'Task001': (10, 3, 5),
    'Task002': 4000000,
    'Task003': 600851475143,
    'Task004': 2,
}


if __name__ == '__main__':
    # print(tasks.task001.__doc__) # Для задачи 001
    # print('Результат: ', str(tasks.task001(task001_const))) # Для задачи 001

    # print(tasks.task002.__doc__)
    # print('Результат: ', tasks.task002(task002_const))

    # print(tasks.task003.__doc__)
    # print('Результат: ', tasks.task003(task003_const)[-1])
    print(tasks.task004.__doc__)
    print('Результат: ', tasks.task004(params['Test004']))

