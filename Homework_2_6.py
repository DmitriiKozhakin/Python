products = int(input('Введите количество позиций товаров , которое вы планирете ввести (2-4)'))
i = 0
my_list = []
name_list = {'название', 'цена', 'количество', 'eд'}
analytic = {'название': [], 'цена': [], 'количество': [], 'eд': []}
while products > i:
    name = input('Введите название товара')
    price = input('Введите цену товара')
    numbers = input('Введите количество товара')
    units = input('Введите еденицу измерения товара')
    my_list.append((i+1, {'название': name, 'цена': price, 'количество': numbers, 'eд': units}))
    for z in name_list:
        tmp = my_list[i][1][z]
        if analytic[z].count(tmp) == 0:
            analytic[z].append(tmp)
    i += 1
print(my_list)
print(analytic)
