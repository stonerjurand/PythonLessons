# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def make_copy():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        copy_name = dir_name.replace('.', '_copy.')
        os.popen(f'copy {dir_name} {copy_name}')
    except FileNotFoundError:
        print("Невозможно найти указанный файл")


def del_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        os.remove(dir_name)
        print(f'файл {dir_name} удален')
    except FileNotFoundError:
        print(f'файл {dir_name} не существует')


def change_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(f'выполнен переход в директорию {dir_name}')
    except FileNotFoundError:
        print(f'директория {dir_name} не существует')


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key](input())
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
