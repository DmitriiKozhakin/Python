a = int(input('Результат в первый день '))
b = int(input('Цель '))
day = 1
while a < b:
    a = float(a * 1.1)
    day += 1
print(day)

