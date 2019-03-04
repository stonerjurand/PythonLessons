# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
import numpy as np


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def ab(self):
        return math.sqrt((self.a[0] - self.b[0])**2+(self.a[1]-self.b[1])**2)

    @property
    def ac(self):
        return math.sqrt((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2)

    @property
    def bc(self):
        return math.sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)

    @property
    def square(self):
        arr = np.array([[self.a[0]-self.c[0], self.a[1]-self.c[1]], [self.b[0]-self.c[0], self.b[1]-self.c[1]]])
        return abs(0.5*np.linalg.det(arr))

    def perimeter(self):
        return self.ab + self.ac + self.bc

    def height(self, base):  # нахождение высоты по основанию
        sides = {
            'ab': self.ab,
            'ac': self.ac,
            'bc': self.bc
        }
        return self.square/sides[base]*2


coords = [[float(i) for i in input(f'Введите координаты точки {j} через зяпятую: ').split(',')] for j in ['A','B','C']]

t = Triangle(*coords)

print(f'Площадь треугольника = {t.square}')
print(f'Периметр треугольника = {t.perimeter()}')
base = input('Введите название стороны основания (AB, AC или BC): ')
print(f'Высота  треугольника по основанию {base} = {t.height(base.lower())}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoscelesTrapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
