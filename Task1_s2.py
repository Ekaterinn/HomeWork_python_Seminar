# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def methodOne():
    numFact = int(input('Введите число '))
    count = 1
    while 1 < numFact:
     count = count * numFact
     numFact-=1
    print(count)

def methodTwo():
    from math import factorial
    numb = int(input('Введите число '))
    print(factorial(numb))
methodOne()