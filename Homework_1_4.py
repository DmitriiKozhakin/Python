val = int(input('Введите число '))
n = val % 10
max_val = n
while n != val % 10:
    n = val % 10
    if n > max_val:
        max_val = n
print(max_val)
