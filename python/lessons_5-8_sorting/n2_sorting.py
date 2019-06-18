# -*- coding: utf-8 -*-
import random
import time


def bubble_sort(array):
    n = len(array)
    swaped = True
    while n > 1 and swaped:
        for i in range(1, n):
            swaped = False
            if array[i-1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swaped = True
        n -= 1
    return array


def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        if i != min:
            array[i], array[min] = array[min], array[i]
    return array


def insertion_sort(array):
    for i in range(len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = x
        i += 1
    return array


def shell_sort(array):
    n = len(array)
    gap = n / 2
    while gap > 0:
        for i in range(int(gap), n):
            temp = array[i]
            j = i
            while j >= gap and array[int(j - gap)] > temp:
                array[int(j)] = array[int(j - gap)]
                j -= gap
                array[int(j)] = temp
        gap /= 2
    return array


def sedgewick_shell_sort(array):
    n = len(array)
    gaps = gengaps(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j - gap]
                j -= gap
                array[j] = temp


def gengaps(n):
    unfinished = True
    gaps = [1]
    k = 1
    while unfinished:
        gap = 4**k+3*2**(k-1)+1
        k += 1
        if gap < n:
            gaps.append(gap)
        else:
            unfinished = False
            gaps.reverse()
    return gaps


def persent_suffle(list, p):
    for i in range(int(len(list)*p/2)):
        a, b = random.randint(0, len(list)-1), random.randint(0, len(list)-1)
        list[a], list[b] = list[b], list[a]
    return list







list = [x for x in range(1000)]
# random.shuffle(list)
suffled = persent_suffle(list, 0.1)


print(suffled)
start_time = time.time()
bubble_sort(suffled)
print(time.time()-start_time)
