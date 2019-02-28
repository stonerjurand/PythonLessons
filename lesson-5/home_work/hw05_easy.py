# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
#from hw05_normal import dir_name

def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'директория {dir_name} создана')
    except FileExistsError:
        print(f'директория {dir_name} уже существует')


def del_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print(f'директория {dir_name} удалена')
    except FileNotFoundError:
        print(f'директория {dir_name} не существует')


if __name__ == "__main__":
    for i in range(1,10):
        dir_name = f'dir_{i}'
        make_dir(dir_name)

    for i in range(1,10):
        dir_name = f'dir_{i}'
        del_dir(dir_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    files = os.listdir(path=os.getcwd())
    folders = [i for i in files if os.path.isdir(os.path.join(os.getcwd(), i))]
    print(folders)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def make_copy():
    file_name = os.path.basename(__file__)
    copy_name = file_name.replace('.', '_copy.')
    os.popen(f'copy {file_name} {copy_name}')
