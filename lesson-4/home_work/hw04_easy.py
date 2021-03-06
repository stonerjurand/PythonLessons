# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

from random import randint

sourceList = [randint(-100, 100) for i in range(10)]

resultList = [i**2 for i in sourceList]

print(sourceList, resultList, sep='\n')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruitsBucket1 = ["Яблоко", "Апельсин", "Персик", "Дыня", "Банан", "Помело", "Рамбутан"]
fruitsBucket2 = ["Слива", "Апельсин", "Персик", "Питайя", "Банан", "Помело", "Финик"]

fruits = [i for i in fruitsBucket1 if i in fruitsBucket2]

print(fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

sourceNumbers = [randint(-100, 100) for i in range(10)]

resultNumbers = [i for i in sourceNumbers if i%3 == 0 and i>0 and not i%4 == 0]

print(sourceNumbers, resultNumbers, sep='\n')