#Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
#Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy
import random

def lIst():
    size = int(input('Введите первую цифру ')),int(input('Введите вторую цифру '))
    numbers = numpy.random.randint(1, 100, size)
    print(numbers)
    print(f"Максимальное число имеет индекс {numpy.argmax(numbers)}")
    print(f"Минимальное число имеет индекс {numpy.argmin(numbers)}")
    print(f'Элементы главной диагонали массива: {numbers.diagonal()}')

    a = numpy.argmax(numbers)
    x = numpy.floor(a/3).astype(int)
    y = a%3
    print(f'Max = {numbers[x][y]}')

    a = numpy.argmin(numbers)
    x = numpy.floor(a/3).astype(int)
    y = a%3
    print(f'Min = {numbers[x][y]}')

    maxvalue = numpy.max(numbers)
    index_line_max, index_line_max = numpy.where(numbers==maxvalue)
    print (index_line_max[0], index_line_max[0])

    minvalue = numpy.min(numbers)
    index_line_min, index_line_min = numpy.where(numbers==minvalue)
    print (index_line_min[0], index_line_min[0])

lIst()