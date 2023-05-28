"Создайте пользовательский аналог метода map()."

"Возвращает список в коотором к каждому жлементу применена функция"
def method(f, col):
    return [f(x) for x in col]
"Возвращает значения прошедшее проверку условия"
def where(f,col):
    return[x for x in col if f(x)]

lIst = [ 1, 5, 43, 34, 345, 64, 456345, 23, 2342, 12]
res = method(int, lIst)
print(res)
res = where(lambda x: x%2==0, res)
print(res)
res = list(method(lambda x: {x,x**2}, res))
print(res)