f_1 = open("File_to_homework_5_4.txt", "r", encoding="utf-8")
translate = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
f_2 = open("File_to_homework_5_4_to_write.txt", "w", encoding="utf-8")
for line in f_1:
    this_line = line.split()
    this_line[0] = translate[this_line[0]]
    print(this_line)
    this_line = ' '.join(this_line)
    f_2.write(f'{this_line}\n')
f_1.close()
f_2.close()
