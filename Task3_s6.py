# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def greaterCommonDivisor(m: int, n: int):
    if m == n:
         return m
    result = 1
    for i in range(2, min(m, n)+1):
         if m % i == 0 and n % i == 0:
             result = i
    return result   
     
def task():
    result = []    
    for i in range(2,12):
        for j in range(1, i):
            if greaterCommonDivisor(i, j) == 1:   
                result.append(str(j) + '/' + str(i))
    return result  