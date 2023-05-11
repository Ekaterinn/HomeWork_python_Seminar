# Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве
# последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random
def rand(N = 15):
    return [random.randint(0,9) for _ in range (N)]

def method(Arr: list, N: int):
    stringArr = ''.join(str(i) for i in Arr)
    index = stringArr.find(str(N))
    if index>=0:
        print(f'Для числа {N} имеется вхождение, индекс: {index}')
    else:
        print(f'Для числа {N} вхождений в списке НЕ имеется') 

Arr = rand()
print (f'Список случайных чисел: {Arr}')

N = int(input('Введите трехзначное число: '))
if N<100 or N>999:
    print(f'Число {N} - не трехзначное!')
else:
    method(Arr,N)