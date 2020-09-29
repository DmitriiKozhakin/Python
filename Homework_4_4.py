# Представлен список чисел. Определить элементы списка,
# не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# def foo():
# list.index(x, [start [, end]])
# Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)


from random import randrange


def foo(array, val):
    try:
        z = array.copy()
        z.remove(val)
        return z.index(val) == -1
    except ValueError:
        return True


arr = []
for i in range(20):
    arr.append(randrange(0, 15))
print(arr)
v_1 = [i for i in arr if foo(arr, i)]
print(v_1)
