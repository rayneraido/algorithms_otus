# -*- coding: utf-8 -*-
import numpy as np


def rec(n):
    if n < 2:
        return 1
    else:
        return rec(n-1) + rec(n-2)


def dinamic(n):
    a = 1
    b = 1
    f = 0
    for i in range(2, n):
        f = a + b
        a = b
        b = f
    return f


def golden(n):
    f = (1 + 5**0.5)/2
    return int((f**n/5**0.5)+0.5)


def matrix(n):
    matrix = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])
    return np.matmul(matrix**n, vec)[0, 0]
