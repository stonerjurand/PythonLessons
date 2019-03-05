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


#coords = [[float(i) for i in input(f'Введите координаты точки {j} через зяпятую: ').split(',')] for j in ['A','B','C']]
coords = [[3.5, 1], [-2, 6], [0, 6]]

t = Triangle(*coords)

print(f'Площадь треугольника = {t.square}')
print(f'Периметр треугольника = {t.perimeter()}')
base = 'AC'  # input('Введите название стороны основания (AB, AC или BC): ')
print(f'Высота  треугольника по основанию {base} = {t.height(base.lower())}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoTrap:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sides = {}

    @property
    def coords(self):
        coords = {'a': self.a, 'b': self.b, 'c': self.c, 'd': self.d}
        return coords

    @property
    def vectors(self):
        vectors = {}
        for key, value in self.coords.items():
            for subkey, subvalue in self.coords.items():
                if subkey != key:
                    vectors[key + subkey] = [subvalue[0] - value[0], subvalue[1] - value[1]]
        return vectors

    @property
    def lenvectors(self):
        lenvectors = {}
        for key, value in self.vectors.items():
            lenvectors[key] = math.sqrt(value[0]**2 + value[1]**2)
        return lenvectors

    def isisotrap(self):
        checklist = []
        base = []
        for key, value in self.vectors.items():
            for subkey, subvalue in self.vectors.items():
                if subkey[0] not in key or subkey[1] not in key:
                    arr = np.array((value, subvalue))
                    if np.linalg.matrix_rank(arr) == 1:
                        checklist.append(True)
                        if key not in base and subkey not in base:
                            base.append(key)
                            base.append(subkey)

        if len(base) == 4:
            if self.lenvectors[base[0][0] + base[1][1]] == self.lenvectors[base[1][0] + base[0][1]]:
                checklist.append(True)
                self.sides.clear()
                self.sides[base[0]] = [self.lenvectors[base[0]], 'base']
                self.sides[base[1]] = [self.lenvectors[base[1]], 'base']
                self.sides[base[0][0] + base[1][0]] = [self.lenvectors[base[0][0] + base[1][0]], 'flank']
                self.sides[base[0][1] + base[1][1]] = [self.lenvectors[base[0][1] + base[1][1]], 'flank']
            else:
                checklist.append(False)
        else:
            checklist.append(False)
        return np.prod(np.array(checklist))

    def lenside(self, side):
        lenside = None
        for key, value in self.sides.items():
            if side[0] in key and side[1] in key:
                lenside = value[0]
        if lenside == None:
            return f'{side} не является стороной равнобочной трапеции'
        else:
            return lenside

    def perimeter(self):
        return sum([i[0] for i in self.sides.values()])

    def square(self):
        bases = [i[0] for i in self.sides.values() if i[1] == 'base']
        flank = sum([i[0] for i in self.sides.values() if i[1] == 'flank'])/2
        return (sum(bases)/2)*math.sqrt(flank**2-((bases[0]-bases[1])**2/4))


#coordstrap = [[float(i) for i in input(f'Введите координаты точки {j} через зяпятую: ').split(',')] for j in ['A','B','C','D']]
coordstrap = [[3, 2], [3, 4], [5, 6], [7, 6]]

trap = IsoTrap(*coordstrap)

if trap.isisotrap():
    print(f'Введены координаты равнобочной трапеции')
    print(f'Площадь равнобочной трапеции = {trap.square()}')
    print(f'Периметр равнобочной трапеции = {trap.perimeter()}')
    side = 'AD'  # input('Введите название стороны: ')
    print(f'Длина стороны {side} = {trap.lenside(side.lower())}')
else:
    print(f'Введенные координаты не соотвествуют равнобочной трапеции')


