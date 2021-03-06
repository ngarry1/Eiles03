#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020
"""Точка входа в проект"""

# import collections
import tasks
from typing import Tuple  # Для задачи 001

params = {
    'Task001': (1000, 3, 5),    # Задача 001
    'Task002': 4000000,         # Задача 002
    'Task003': 600851475143,    # Задача 003
    'Task004': 1000,            # Задача 004
    'Task005': 20,              # Задача 005
    'Task006': 100,             # Задача 006
    'Task007': 10001,           # Задача 007
}


if __name__ == '__main__':
    # print(tasks.task001.__doc__)
    # try:
    #     print('Результат: ', str(tasks.task001(params['Task001'])))
    # except KeyError:
    #     print('Ошибка в параметрах задачи 001')

    # print(tasks.task002.__doc__)
    # try:
    #     print('Результат: ', tasks.task002(params['Task002']))
    # except KeyError:
    #     print('Ошибка в параметрах задачи 002')

    # print(tasks.task003.__doc__)
    # try:
    #     print('Результат: ', tasks.task003(params['Task003'])[-1])
    # except KeyError:
    #     print('Ошибка в параметрах задачи 003')

    # print(tasks.task004.__doc__)
    # try:
    #     print('Результат: ', tasks.task004(params['Task004']))
    # except KeyError:
    #     print('Ошибка в параметрах задачи 004')

    # print(tasks.task005.__doc__)
    # try:
    #     print('Результат: ', tasks.task005(params['Task005']))
    # except KeyError:
    #     print('Ошибка в параметрах задачи 005')
    #
    # print(tasks.task006.__doc__)
    # try:
    #     print('Результат: ', tasks.task006(params['Task006']))
    # except KeyError:
    #     print('Ошибка в параметрах задачи 006')

    # print(tasks.prime.__doc__)
    # try:
    #     print('Число: ', tasks.prime(params['Task007'])[-1])
    #     print('Индекс в списке: ', len(tasks.prime(params['Task007'])))
    # except KeyError:
    #     print('Ошибка в параметрах задачи 007')

    print(tasks.task007.__doc__)
    try:
        print('Результат: ', tasks.task007(params['Task007']))
    except KeyError:
        print('Ошибка в параметрах задачи 007')
