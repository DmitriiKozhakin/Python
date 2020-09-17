words = input('Введите несколько слов через пробел').split()
for n, i in enumerate(words, 1):
    print(n, str(i)[:10])
