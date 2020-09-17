l = list(input('Введите несколько элементов'))
length = len(l)
temp = ''
for i in range(1, length, 2):
    temp = l[i]
    l[i] = l[i - 1]
    l[i - 1] = temp
print(l)
