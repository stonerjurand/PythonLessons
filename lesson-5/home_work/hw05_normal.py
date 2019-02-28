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
import re
import hw05_easy as e


def dir_into(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(f'выполнен переход в директорию {dir_name}')
    except FileNotFoundError:
        print(f'директория {dir_name} не существует')


def dir_out():
    cur_path = os.getcwd()
    cur_path = re.split(r'\\', cur_path)
    dist_path = '/'.join(cur_path[:-1])
    os.chdir(dist_path)
    print(f'выполнен выход в директорию {cur_path[-2]}')


def list_dir():
    content = os.listdir(path=os.getcwd())
    print(content)


while True:
    print('Текущая директория = ', os.getcwd())
    key = input(
        "Введите команду из списка:\n"
        "1. Перейти в директорию - dirinto\n"
        "2. Выйти из директории - dirout\n"
        "3. Просмотреть содержимое текущей директории - ls\n"
        "4. Удалить директорию - del\n"
        "5. Создать директорию - mkdir\n"
        "6. Выйти из программы - exit\n"
    )
    if key == 'exit':
        sys.exit()

    if key == 'mkdir':
        dir_name = input('Введите название директории: ')
        e.make_dir(dir_name)

    if key == 'del':
        dir_name = input('Введите название директори: ')
        e.del_dir(dir_name)

    if key == 'dirinto':
        dir_name = input('Введите название директории: ')
        dir_into(dir_name)

    if key == 'dirout':
        dir_out()

    if key == 'ls':
        list_dir()
