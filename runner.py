#!/usr/bin/env python
# -*- encoding: utf-8 -*-d

# Created at 11.06.2020

import func_task
from typing import Tuple

task001_const: Tuple[int, int, int] = (10, 3, 5)

if __name__ == '__main__':
    print(func_task.task01.__doc__)
    print('Результат: ', str(func_task.task01(task001_const)))
