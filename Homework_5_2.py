f_1 = open("File_to_homework_5_2.txt", "r", encoding="utf-8")
lines = 0
for line in f_1:
    print(f'Символов в строке {lines+1}  = {len(line)}')
    lines += 1
print(f'Количество строк в файле = {lines}')
f_1.close()


