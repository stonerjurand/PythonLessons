# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import hw05_easy as e


while True:
    print('Текущая директория = ', os.getcwd())
    key = input(
        "Введите команду из списка:\n"
        "1. Перейти в папку - chdir <имя папки>\n"
        "2. Просмотреть содержимое текущей папки - ls\n"
        "3. Удалить папку - del <имя папки>\n"
        "4. Создать папку - mkdir <имя папки>\n"
        "5. Выйти из программы - exit\n"
    )
    key = key.split(' ')
    if key[0] == 'exit':
        sys.exit()

    if key[0] == 'mkdir':
        try:
            #global dir_name
            dir_name = key[1]
            e.make_dir(dir_name)
        except IndexError:
            print("Необходимо указать имя директории вторым параметром")


# key = 'mkdir newDir'
# print(key.split(' '))