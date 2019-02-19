# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

for fruit in fruits:
    print(str(fruits.index(fruit)+1) + '.' + '{:>10}'.format(fruit))  # решение без enumerate()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

firstList = [1, 2, 3, True, 'name', 'somestring', 1]
secondList = [0, 1, 4, False, 'name']

for element in firstList[:]:  # итерация через копию исходного списка
    if element in secondList:
        firstList.remove(element)

print(firstList)  # True == 1

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

sourceList = [1, 6, 10, 15, 365, 12, 84, 98, 2]

resultList = []

for element in sourceList:
    if element % 2 == 0:
        resultList.append(element/4)
    else:
        resultList.append(element*2)

print(resultList)
