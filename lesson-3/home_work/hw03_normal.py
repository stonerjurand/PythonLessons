 # Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1,1]
    while len(fib) < m:
        fib.append(sum(fib[-2:]))
    return fib[n:m]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(func, array):
    for i in array[::]:
        if func(i) == False:
            array.remove(i)
    return array


array = [1,2,3,4,5,6,7]
print(filter_func(lambda x: x > 5, array))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

from random import randint

A1 = [-2, 4]  # [randint(-100, 100) for i in range(2)]
A2 = [-2, -3]  # [randint(-100, 100) for i in range(2)]
A3 = [2, -1]  # [randint(-100, 100) for i in range(2)]
A4 = [2, 6]  # [randint(-100, 100) for i in range(2)]

axes_values = list(zip(A1, A2, A3, A4))

sortedX = sorted(axes_values[0])
sortedY = sorted(axes_values[1])

if sortedX[0] + sortedX[3] == sortedX[1] + sortedX[2] and sortedY[0] + sortedY[3] == sortedY[1] + sortedY[2]:
    print('Данные точки являются вершинами параллелограмма')
else:
    print('Данные точки не являются вершинами параллелограмма')

