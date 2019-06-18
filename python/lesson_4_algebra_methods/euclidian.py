# -*- coding: utf-8 -*-
import time


def euclidian_substruction(a, b):
    """
    Алгоритм Евклида поиска наибольшего общего делителя исходной пары через вычитание
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def euclidian_mod(a, b):
    """
    Алгоритм Евклида поиска наибольшего общего делителя исходной пары через остаток от деления
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a


def euclidian_recursion(a, b):
    """
    Алгоритм Евклида поиска наибольшего общего делителя рекурсией
    """
    if b == 0:
        return a
    return euclidian_recursion(b, a % b)


start_time = time.time()
euclidian_recursion(1234567890, 12)
print(time.time() - start_time)
