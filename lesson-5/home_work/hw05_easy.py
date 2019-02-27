# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
#from hw05_normal import dir_name

def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'директория {dir_name} создана')
    except FileExistsError:
        print(f'директория {dir_name} уже существует')

if __name__ == "__main__":
    for i in range(1,10):
        dir_name = f'dir_{i}'
        make_dir()




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    files = os.listdir(path=os.getcwd())
    print(files)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def make_copy():
    cur_path = sys.argv[0].split('/')
    file_name = cur_path[-1]
    copy_name = file_name.replace('.', '_copy.')
    os.popen(f'copy {file_name} {copy_name}')

# try:
#     dir_name = sys.argv[1]
# except IndexError:
#     dir_name = None
