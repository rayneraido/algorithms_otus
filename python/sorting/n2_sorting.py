# -*- coding: utf-8 -*-


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

