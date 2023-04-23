#Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
#60 -> 2, 2, 3, 5

num = int(input("Введите число: "))
i = 2  # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")