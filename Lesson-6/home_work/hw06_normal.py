# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:
    def __init__(self, name, patronymic, surname, birth_date, school):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def get_short_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0] + '.'

    def set_name(self, new_name):
        self.name = new_name


class Parent(People):
    def __init__(self, name, patronymic, surname, birth_date, school, children):
        People.__init__(self, name, patronymic, surname, birth_date, school)
        self.children = [children]

    def set_child(self, name, patronymic, surname):
        self.children.append([name, patronymic, surname])

    def get_names_of_children(self):
        return [self.children[i][2]+' '+self.children[i][0]+' '+self.children[i][1] for i in range(len(self.children))]


class Student(People):
    def __init__(self, name, patronymic, surname, birth_date, school, class_room):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, patronymic, surname, birth_date, school)
        # Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}


    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(People):
    def __init__(self, name, patronymic, surname, birth_date, school, teach_classes, specialty):
        People.__init__(self, name, patronymic, surname, birth_date, school)
        self.teach_classes = teach_classes
        self.specialty = specialty


students = [Student("Александр", 'Петрович', "Иванов", '10.11.1998', "8 гимназия", "5 А"),
            Student("Петр", "Евгеньевич", "Сидоров", '10.01.1995', "8 гимназия", "8 Б"),
            Student("Иван", "Васильевич", "Петров", '12.11.1999', "8 гимназия", "4 В"),
            Student("Мария", "Ивановна", "Глебова", '06.08.1999', "8 гимназия", "4 В")
            ]

parents =  [Parent("Петр", 'Михайлович', "Иванов", '11.05.1958', "8 гимназия", ["Александр", 'Петрович', "Иванов"]),
            Parent("Ольга", 'Юрьевна', "Иванова", '01.02.1962', "8 гимназия", ["Александр", 'Петрович', "Иванов"]),
            Parent("Евгений", "Иванович", "Сидоров", '10.03.1960', "8 гимназия", ["Петр", "Евгеньевич", "Сидоров"]),
            Parent("Светлана", "Евгеньевна", "Сидорова", '23.11.1961', "8 гимназия", ["Петр", "Евгеньевич", "Сидоров"]),
            Parent("Василий", "Григорьевич", "Петров", '30.11.1975', "8 гимназия", ["Иван", "Васильевич", "Петров"]),
            Parent("Виктория", "Петровна", "Петрова", '09.10.1975', "8 гимназия", ["Иван", "Васильевич", "Петров"]),
            Parent("Иван", "Иванович", "Глебов", '07.06.1968', "8 гимназия", ["Мария", "Ивановна", "Глебова"]),
            Parent("Валерия", "Михайловна", "Глебова", '19.01.1971', "8 гимназия", ["Мария", "Ивановна", "Глебова"])
            ]

teachers = [Teacher("Владимир", 'Петрович', "Сомин", '20.09.1969', "8 гимназия", ["5 А", "8 Б", "4 В"], 'русский язык'),
            Teacher("Светлана", "Павловна", "Белова", '10.01.1981', "8 гимназия", ["8 Б"], 'физика'),
            Teacher("Иван", "Васильевич", "Петров", '12.11.1979', "8 гимназия", ["5 А", "4 В"], 'математика'),
            ]


school = "8 гимназия"  # input('Введите название школы: ')
classrooms = list(set([i.class_room for i in students if i.school == school]))
print(f'Все классы школы {school}:', classrooms, sep='\n')

class_room = '4 В'  # input('Введите название класса: ')
studs = [i.get_short_name() for i in students if i.class_room == class_room]
print(f'Все ученики {class_room} класса:', studs, sep='\n')

student = 'Иванов Александр Петрович'  # input('Введите полное ФИО ученика: ')
cl_room = [i.class_room for i in students if i.get_full_name() == student]
specialties = [i.specialty for i in teachers if cl_room[0] in i.teach_classes]
print(f'Все предметы ученика {student}:', specialties, sep='\n')

child = 'Иванов Александр Петрович'  # input('Введите полное ФИО ученика: ')
parentsOfChild = [i.get_full_name() for i in parents if child in i.get_names_of_children()]
print(f'Родители ученика {child}:', parentsOfChild, sep='\n')

cl_room2 = '4 В'  # input('Введите название класса: ')
tchers = [i.get_full_name() for i in teachers if cl_room2 in i.teach_classes]
print(f'Учителя, преподающие в {cl_room2} классе:', tchers, sep='\n')
