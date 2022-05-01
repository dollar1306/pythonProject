from math import sqrt

from work_python_testers.lesson_3.sum_module import sum_list


def sqrt_nums(numbers):
    sum = sum_list(numbers)
    return sqrt(sum)