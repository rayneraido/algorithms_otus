# -*- coding: utf-8 -*-
import time


def power(base, power):
    """
    Алгоритм возведения в степень: итеративный (n умножений)
    """
    for _ in range(1, power):
        base *= base
    return base


def power_of_two(base, power):
    """
    Алгоритм возведения в степень: через степень двойки с домножением
    """
    a = 1
    while power > 1:
        if power % 2 == 1:
            a *= base
        base *= base
        power /= 2
    if power > 0:
        a *= base
    return a


def binary_power(base, power):
    """
    Алгоритм возведения в степень: через двоичное разложение показателя степени.
    """
    

print (power(2,2))