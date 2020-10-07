# Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм
# валидации вводимых пользователем данных. Например, для указания
# количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать
# в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Exc(Exception):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    def __init__(self, goodsstock, goodssub):
        self.goodsstock = goodsstock
        self.goodssub = goodssub

    def takegoods(self, orgtech, quantites, par):

        try:
            if quantites.isdigit() == False and quantites.replace('-', '').isdigit() == False:
                raise Exc('Введённый элемент не попадёт в список так как это не число ')
            quantites = int(quantites)
            if par in self.goodsstock.keys():
                if orgtech.model in self.goodsstock[par]:
                    self.goodsstock[par][orgtech.model] += int(quantites)
                else:
                    self.goodsstock[par][orgtech.model] = int(quantites)
            else:
                self.goodsstock[par] = {}
                self.goodsstock[par][orgtech.model] = int(quantites)
            print(f' на складе {self.goodsstock}')

        except (ValueError, Exc) as err:
            print(err)

    def takeaway(self, orgtech, quantites, par):
        try:
            if quantites.isdigit() == False and quantites.replace('-', '').isdigit() == False:
                raise Exc('Введённый элемент не попадёт в список так как это не число ')
            quantites = int(quantites)
            if par in self.goodsstock.keys():
                if orgtech.model in self.goodsstock[par]:
                    if self.goodsstock[par][orgtech.model] < quantites:
                        raise Exc('Нет столько товара на складе')
                    else:
                        self.goodsstock[par][orgtech.model] -= quantites
                        if par in self.goodssub.keys():
                            if orgtech.model in self.goodssub[par]:
                                self.goodssub[par][orgtech.model] += quantites
                            else:
                                self.goodssub[par][orgtech.model] = quantites
                        else:
                            self.goodssub[par] = {}
                            self.goodssub[par][orgtech.model] = quantites
                        print(f' на складе {self.goodsstock}')
                else:
                    raise Exc('Нет  такой марки товара на складе')
            else:
                raise Exc('Нет  такого типа товара на складе')

        except (ValueError, Exc) as err:
            print(err)
        else:
            print(f' на складе {self.goodsstock}')
            print(f' в подразделении  {self.goodssub}')


class Tech:
    def __init__(self, model, price):
        self.model = model
        self.avgPrice = price


class Printer(Tech):
    def __init__(self, model, price, printpermin):
        super().__init__(model, price)
        self.printpermin = printpermin


class Scanner(Tech):
    def __init__(self, model, price, scanpermin):
        super().__init__(model, price)
        self.scanpermin = scanpermin


class Xerox(Tech):
    def __init__(self, model, price, xeroxpermin):
        super().__init__(model, price)
        self.xeroxpermin = xeroxpermin


stock = Stock({}, {})
P1 = Printer('LG-300', 25000, 60)
S1 = Scanner('HP-225Z8', 34999, 10)
X1 = Xerox('Microsoft_blue_sky', 50000, 300)
P2 = Printer('LG-00', 2500, 6)
S2 = Scanner('HP-55', 10099, 5)
X2 = Xerox('Microsoft_red_cat', 900000, 600)
P3 = Printer('LG-Ultra', 250000, 600)
S3 = Scanner('HP-!', 4999, 20)
X3 = Xerox('Microsoft_pink_fox', 10000, 100)

vals = {'X1': X1, 'X2': X3, 'X3': X3, 'P1': P1, 'P2': P2, 'P3': P3, 'S1': S1, 'S2': S2, 'S3': S3}
print('Добро пожаловать на склад')
while True:
    print('Хотите отправить товары на склад или со склада в подразделение ?')
    answer_1 = input('Введите + для отправки на склад или - для отправки со склада в подразделение либо q для выхода')

    if answer_1 in ['+', '-']:
        answer_2 = input('Введите P/S/X1-3 например X1 или S3 для выбора модели для отправки или введите q ')
        answer_3 = input('Введите количество единиц товара , например 1 , 6 , или 10 либо введите q')

        try:
            if answer_2 not in vals.keys():
                raise Exc('Вы ввели товар которого нет в системе')
            if answer_1 == '+':
                stock.takegoods(vals[answer_2], answer_3, vals[answer_2].__class__.__name__)
            else:
                stock.takeaway(vals[answer_2], answer_3, vals[answer_2].__class__.__name__)

        except (ValueError, Exc) as err:
            print(err)

    if answer_1 == 'q':
        break
