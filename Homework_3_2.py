# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def foo(name, surname, date_birth, city, email, phone):
    return f"Имя: {name}, Фамилия: {surname}, День рождения: {date_birth} , Город: {city}, Почта: {email}, Тел.:{phone}"


print(foo(name='Alex', surname='Smirnov', date_birth='01.01.1988', city='Moscow', phone='7-666-555-22-11',
          email='as@list.ru', ))
