# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
from functools import lru_cache
 
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
 
num = int(input('Введите число '))
print ([fib(n) for n in range(num)])