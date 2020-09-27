f_1 = open("File_to_homework_5_3.txt", "r", encoding="utf-8")
salaryList = []
for line in f_1:
    this_line = line.split()
    salaryList.append(this_line[1])
    if float(this_line[1]) < 20000:
        print(f'У Сотрудника {this_line[0]} зарпата меньше 20000')


def avg(list):
    avgSum = 0
    for sum in list:
        avgSum += float(sum)
    return round(avgSum / len(list), 2)


print(f'Средняя ЗП {avg(salaryList)}')
