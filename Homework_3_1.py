# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def foo(val1, val2):
    if val2 != 0 and val1.isdigit() and val2.isdigit():
        return round(int(val1) / int(val2), 2)
    else:
        return 0


val1 = input('Введите первое число')
val2 = input('Введите второе число')

val3 = foo(val1, val2)
print(val3)
