"Создайте декоратор, повторяющий функцию заданное количество раз."

import random
def decor(amt: int):
    def repead(*args, **kwargs):
        res = []
        for _ in range(amt):
          res.append(random.randint(1,10))
        print(res, f"Функция повторяется {len(res)} раз", sep="\n")
    return repead

@decor(amt=int(input("Cколько раз повторить функцию: ")))
def my_func(decor):
    return