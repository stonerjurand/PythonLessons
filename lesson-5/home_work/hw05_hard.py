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
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not pointer:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), pointer)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(pointer))
    except FileExistsError:
        print('директория {} уже существует'.format(pointer))


def make_copy():
    if not pointer:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        copy_name = pointer.replace('.', '_copy.')
        os.popen(f'copy {pointer} {copy_name}')
        print(f'Файл скопирован под именем {copy_name}')
    except FileNotFoundError:
        print("Невозможно найти указанный файл")


def del_file():
    if not pointer:
        print("Необходимо указать имя файла вторым параметром")
        return
    answer = input('Вы уверены? [Y/N]: ')
    if answer == 'Y':
        try:
            os.remove(pointer)
            print(f'файл {pointer} удален')
        except FileNotFoundError:
            print(f'файл {pointer} не существует')


def change_dir():
    if not pointer:
        print("Необходимо указать путь")
        return
    try:
        if os.path.isabs(pointer):
            os.chdir(pointer)
        else:
            dir_path = os.path.join(os.getcwd(), pointer)
            os.chdir(dir_path)
        print(f'выполнен переход в директорию {pointer}')
    except NotADirectoryError:
        print(f'директория {pointer} не существует')


def print_path():
    print(os.getcwd())

def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': make_copy,
    'rm': del_file,
    'cd': change_dir,
    'ls': print_path
}

try:
    pointer = sys.argv[2]
except IndexError:
    pointer = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
