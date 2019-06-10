# -*- coding: utf-8 -*-
import time


def euclidian(a, b):
    """
    нахождение наибольшего общего делителя исходной пары
    """
    start_time = time.time()
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    work_time = time.time() - start_time
    print(work_time)
    return a


def euclidian_2(a, b):
    """
    второй вариант
    """
    start_time = time.time()
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    work_time = time.time() - start_time
    print(work_time)
    return a


def euclidian_recursion(a, b):
    """
    второй вариант с рекурсией
    """
    if b == 0:
        return a
    return euclidian_recursion(b, a % b)

# 8.529384851455688 ms 6 1234567890, 12
# 2.1457672119140625e-06
print(euclidian_recursion(1234567890, 12))

