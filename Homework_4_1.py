from sys import argv
from math import isfinite


def foo():
    try:
        val = [float(i) for i in argv[1:] if isfinite(float(i))]
        print(f'Salary {val[0] * val[1] + val[2]}')

    except ValueError:
        print('Error. U need 3 number params')


foo()
