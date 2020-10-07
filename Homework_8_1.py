# Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, param):
        self.param = param

    @classmethod
    def m_1(cls, param):
        try:
            fdate = param.split('-')
            dd, mm, yyyy = int(fdate[0]), int(fdate[1]), int(fdate[2])
            cls.m_2(cls, dd, mm, yyyy)
        except ValueError:
            print('Неверный формат даты')
        else:
            print(f'{dd, mm, yyyy}')

    @staticmethod
    def m_2(self, dd, mm, yyyy):
        if mm == 0 or mm > 12:
            print('Неверный месяц')
        if dd == 0 or dd > 31:
            print('Неверный День')
        if yyyy == 0:
            print('Неверный Год')


d_1 = input('Введите дату в формате "dd-mm-yyyy"')
Data(d_1).m_1(d_1)
