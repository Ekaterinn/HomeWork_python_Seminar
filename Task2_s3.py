# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
my_list = []
my_list.append(input('Введите названия десяти фруктов'))
count = 0
while count < 10:
    my_list.append(str(input()))
    count = count+1
print(my_list)
check = 'А'
res = [idx for idx in my_list if idx[0].lower() == check.lower()]
print(res)