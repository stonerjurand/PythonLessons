__author__ = 'Резников Юранд Григорьевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number = int(input())

max = 0

while number > 0:
    n = number % 10
    if n > max:
        max = n
    number = number//10
print(int(max))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('Введите значение переменной "a" '))
b = int(input('Введите значение переменной "b" '))
a, b = b, a
print('a = ' + str(a) + '\n' + 'b = ' + str(b))

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Введите значение коэффициента "a" '))
b = int(input('Введите значение коэффициента "b" '))
c = int(input('Введите значение коэффициента "c" '))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('x1 = ' + str(x1) + '\n' + 'x2 = ' + str(x2))
elif D == 0:
    x = -b/(2 * a)
    print('x = ' + str(x))
else:
    print('Уравнение не имеет действительных корней')