count_m = 0
count_i = 0
my_list = [7, 5, 3]
el_ind = 0
while count_m < 6:
    element = input('Введите число')
    if element.isdigit():
        element = int(element)
        count_i = 0
        for n, i in enumerate(my_list, 1):
            if i < element:
                my_list.insert(count_i, int(element))
                break
            elif i == element:
                my_list.insert(count_i + my_list.count(element), element)
                break
            elif len(my_list) == n:
                my_list.insert(n, element)
                break
            count_i += 1
    else:
        print('Error')
    print(my_list)
    count_m += 1
