# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, par):
        self.par = par

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation + other.calculation


class Coat(Clothes):

    @property
    def calculation(self):
        result = (self.par / 6.5 + 0.5)
        print(result)
        return result


class Suit(Clothes):

    @property
    def calculation(self):
        result = (2 * self.par + 0.3) / 100
        print(result)
        return result


c1 = Coat(5)
s1 = Suit(180)

print(round(c1 + s1, 2))
