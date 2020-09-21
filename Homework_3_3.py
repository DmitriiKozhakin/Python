# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(val1, val2, val3):
    def foo(*args):
        return min(args)

    minval = foo(val1, val2, val3)
    return val1 + val2 + val3 - minval


try:
    print(my_func(int(input('Введите число 1')), int(input('Введите число 3')), int(input('Введите число 3'))))
except ValueError:
    print('Ошибка')
