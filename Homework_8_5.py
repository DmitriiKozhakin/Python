class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        z = f'{a} + {b}* i'

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'z = {self.a * other.a - self.b * other.b}  + {self.a * other.b + other.a*self.b }* i'

        #z1⋅z2=(x1+y1i)⋅(x2+y2i)=(x1⋅x2−y1⋅y2)+(x1⋅y2+x2⋅y1)i


c1 = Complex(1, 2)
c2 = Complex(5, 6)
print(c1+c2)
print(c1*c2)