# Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar
# и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from random import randint


class Car:
    directions = {'0': 'Влево', '1': 'Вправо'}

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали')

    def stop(self):
        print('Встали')

    def turn(self, direction):
        print(f'Повернули {self.directions[direction]}')

    def show_speed(self):
        print(f'Скорость  {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed < 60:
            print(f'Скорость  {self.speed}')
        else:
            print('Превышаем')


class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            print(f'Скорость  {self.speed}')
        else:
            print('Превышаем')


# = Car(60, 'Красный', 'Жигули', False)
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


# = Car(250, 'Голубой', 'БМВ', True)
print(f'TownCar start')
TC = TownCar(61, 'Белый', 'ДЭУ', False)
TC.go()
TC.turn(str(randint(0, 1)))
TC.stop()
TC.show_speed()

print(f'TownCar end')

print(f'SportCar start')
SC = SportCar(300, 'Фиолетовый', 'АУДИ', False)
SC.go()
SC.turn(str(randint(0, 1)))
SC.stop()
SC.show_speed()

print(f'SportCar end')

print(f'WorkCar start')
WC = WorkCar(41, 'Красный', 'Жигули', False)
WC.go()
WC.turn(str(randint(0, 1)))
WC.stop()
WC.show_speed()

print(f'WorkCar end')

print(f'PoliceCar start')
PC = PoliceCar(250, 'Голубой', 'БМВ')
PC.go()
PC.turn(str(randint(0, 1)))
PC.stop()
PC.show_speed()
print(f'PoliceCar end')
