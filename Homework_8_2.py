class Exc(Exception):
    def __init__(self, txt):
        self.txt = txt


i = input('Введите первое число')
j = input('Введите второе число')

try:
    v_1, v_2 = int(i), int(j)
    if v_2 == 0:
        raise Exc('Нельзя делить на ноль')
except(ValueError, Exc) as err:
    print(err)
else:
    print(v_1 / v_2)
finally:
    print('Конец обработки')
