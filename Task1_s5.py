# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random
def lIst():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num)

def sort(num):
    arr = list (filter(lambda arr: arr > 5, num))
    return print(arr)

lIst()