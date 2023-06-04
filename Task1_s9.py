#Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy
import random

def lIst():
    size = int(input('Из скольки чисел составить список? Введите цифру '))
    numbers = numpy.random.randint(1, 100, size)
    unique_elements = numpy.unique(numbers)
    print(numbers)
    print(unique_elements)
    print(f"Уникальных элементов {len(unique_elements)}")
lIst()