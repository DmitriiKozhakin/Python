import json as j

res = [{}]
f_1 = open("text_7.txt", "r", encoding="utf-8")
Homework_5_7_result = open("Homework_5_7_result.json", "w", encoding="utf-8")


def foo(el_prev, el):
    return el_prev + el


sum_tmp = 0
for line in f_1:
    val = line.split()
    profit = int(val[2]) - int(val[3])
    if profit > 0:
        res[0].update({val[0]: profit})
        sum_tmp += profit
res.append({'avg': sum_tmp / len(res)})

j.dump(res, Homework_5_7_result, ensure_ascii=False)
f_1.close()
Homework_5_7_result.close()
