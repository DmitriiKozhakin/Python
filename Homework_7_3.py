import math


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'сумма {self.cell + other.cell}'

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return f'разница {self.cell - other.cell}'
        else:
            return f'разница не может быть отрицательной'

    def __mul__(self, other):
        return f'произведение  {self.cell * other.cell}'

    def __floordiv__(self, other):
        return f'деление {self.cell // other.cell}'

    def make_order(self, rows):
        for i in range(math.floor(self.cell / rows)):
            print(f'{rows * "*"}')
        if self.cell % rows > 0:
            print(self.cell % rows * '*')


с_1 = Cell(15)
с_2 = Cell(14)

print(с_1 + с_2)
print(с_1 - с_2)
print(с_2 - с_1)
print(с_2 * с_1)
print(с_2 // с_1)
print(с_1 // с_2)

print(с_1.make_order(4))
