#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 23.06.2020
# from typing import Tuple


def test_task01():
    """ Тест задачи 001"""

    task001_const: list = [10, 3, 5]
    number_sum: int = 0

    for num in range(3, task001_const[0]):
        if (num % task001_const[1] == 0) or (num % task001_const[2] == 0):
            number_sum += num
    assert number_sum == 23
