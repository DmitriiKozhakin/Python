f_1 = open("text_6.txt", "r", encoding="utf-8")
res = {}
for line in f_1:
    val = line.split(':')
    name = val[0]
    times = val[1].split(' ')
    final_sum = 0
    for i in times:
        tmp_sum = ''
        for z in i:
            if z.isdigit():
                tmp_sum += z
        if tmp_sum != '':
            final_sum += int(tmp_sum)
    res[name] = final_sum
print(res)
