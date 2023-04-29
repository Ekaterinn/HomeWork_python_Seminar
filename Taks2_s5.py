# Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
import random
def lIst():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num)

def sort(num):
    arr = []
    for i in range(len(num)):
        if num[i] == max(num[:i+1:]) and num[i] not in arr:
            arr.append(num[i])
    return print(arr)
lIst()