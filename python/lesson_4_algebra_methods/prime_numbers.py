# -*- coding: utf-8 -*-
import time


def get_primes(N):
    """
    Алгоритмы поиска кол-ва простых чисел до N через перебор делителей
    """
    primes = []
    for i in range(1, N):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def get_primes_sqrt(N):
    """
    Алгоритмы поиска кол-ва простых чисел до N через перебор делителей
    """
    primes = []
    for i in range(1, N):
        for j in range(2, int(i**0.5)):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def get_primes_sqrt_odds(N):
    """
    Алгоритмы поиска кол-ва простых чисел до N через перебор делителей
    """
    primes = []
    for i in range(1, N):
        for j in range(1, int(i**0.5), 2):
            if i % j == 0 and j != 1:
                break
        else:
            primes.append(i)
    return primes


def sieve_of_eratosthenes(n):
    """
    Решето Эратосфена
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            print(p)
