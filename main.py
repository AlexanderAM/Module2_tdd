import math


def square_root(num):
    try:
        num = float(num)
    except ValueError:
        num = 0
    return math.sqrt(num)


def quadratic_equation(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError:
        return None, None
    d = b**2 - 4 * a * c
    try:
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
        elif d == 0:
            x1 = -b / (2 * a)
            x2 = None
        else:
            x1 = x2 = None
    except ZeroDivisionError:
        x1 = x2 = None
    return x1, x2


def bubble_sort(array):
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return array


def shell_sort(array):
    n = len(array)
    if n == 0:
        return []
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

