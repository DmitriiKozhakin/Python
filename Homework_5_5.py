import random as r

f_1 = open("File_to_homework_5_5.txt", "w", encoding="utf-8")
summary = 0
for i in range(15):
    el = r.random() * 10
    f_1.write(str(el) + " ")
    summary += el
print(f'Сумма = {summary}')
f_1.close()
