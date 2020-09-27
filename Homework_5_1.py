f_1 = open("f_1.txt", "w", encoding="utf-8")
x = "continue"
c = 0
while x != '':
    x = input('Введите слово')
    if not x:
        break
    f_1.write(x+'\n')
f_1 = open("f_1.txt", "r", encoding="utf-8")
for line in f_1:
    print(line)
f_1.close()
