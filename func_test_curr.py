#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 25.08.2020
from typing import List
import pytest


def test_task007():
    """ Тест задачи 007
    Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
    Очевидно, что 6 - ое простое число - 13.

    Какое число является 10001 - ым простым числом?"""

    test_list: List[int] = [2, 3, 5, 7, 11, 13]
    count: int = 6

    number: int = 15
    lst: List[int] = []

    for i in range(2, number + 1):
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

    for l in test_list:
        assert test_list[l] == lst

    assert count == len(test_list)

    return lst

test_task007()
