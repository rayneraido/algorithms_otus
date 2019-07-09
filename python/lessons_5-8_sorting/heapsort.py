# -*- coding: utf-8 -*-
import math


def drown(heap, i, size):
    l = (i*2)+1
    r = (i*2)+2
    largest = i
    if l <= size-1 and heap[l] > heap[i]:
        largest = l

    if r <= size-1 and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        drown(heap, largest, size)
    return heap


def build_heap(array):
    for i in range(int(math.floor((len(array)-1)/2)), -1, -1):
        drown(array, i, len(array))
    return array


def remove_element(heap, i):
    element = heap[i]
    heap[i] = heap[len(heap) - 1]
    del heap[-1]
    drown(heap, i, len(heap))
    return element


def heap_sort(array):
    array = build_heap(array)
    for i in range(len(array)-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        array = drown(array, 0, i)
    return array
