#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 27.08.2020
from typing import List
import math


def prime(number) -> List[int]:
    """Список всех простых чисел в диапазоне 1 - N

        :param number: Натуральное число в диапазоне 1 - N
        :type number: int
        :return: List[int]>

    """

    lst = [2]
    for i in range(3, number + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j > int((math.sqrt(i)) + 1):
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)

    return lst

# --------------------------------------------------------------------


