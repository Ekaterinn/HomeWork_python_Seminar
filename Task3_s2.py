#Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
#«one» «onetwonine» - o – 2, n – 3, e – 2
strOne = input('Введите строку: ')
strTwo = input('Введите значения: ')
len_one = len(strOne)
len_two = len(strTwo)
count = 0
for i in range(len_one):
    count = 0
    for j in range(len_two):
        if  strOne[i]== strTwo[j]:
            count+=1
    print(f'{strOne[i]}-{count}')
