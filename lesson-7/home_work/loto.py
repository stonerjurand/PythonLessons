#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import sys


class Cask:
    def __init__(self):
        self.l = [i for i in range(1, 91)]
    def get(self):
        n = random.choice(self.l)
        self.l.remove(n)
        print()
        print(f'Новый бочонок: {n} (осталось {len(self.l)})')
        yield n


class Loto:

    def gen_card(self):
        card = [[' ' for i in range(9)] for j in range(3)]

        cardnumbers = [i for i in range(1,91)]

        for line in card:
            coords = [i for i in range(9)]
            linecoords = []
            numbers = []
            for i in range(5):
                num = random.choice(coords)
                linecoords.append(num)
                coords.remove(num)
                number = random.choice(cardnumbers)
                numbers.append(number)
                cardnumbers.remove(number)
            numbers = list(sorted(numbers))
            linecoords = list(sorted(linecoords))
            for i in range(len(numbers)):
                line[linecoords[i]] = numbers[i]
        return card

    def get_card(self, player):
        print()
        print('{:-^25}'.format(player.name))
        for line in player.card:
            print(*line)
        print('{:-^25}'.format('-'))

    def check(self, player, cask_number):
        checkbox = 0
        for line in player.card:
            for index, value in enumerate(line):
                if value == cask_number:
                    line[index] = '-'
                    player.score += 1
                    if player.score == 15:
                        print(f'{player.name} выиграла!')
                        sys.exit()
                    checkbox = 1
        return bool(checkbox)



class Player(Loto):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.card = self.gen_card()


game = Loto()
cask = Cask()
player = Player('Ваша карточка')
comp = Player('Карточка компьютера')

while True:
    num_cask = next(cask.get())
    game.get_card(player)
    game.get_card(comp)

    inp_user = input('Зачеркнуть цифру? (y/n)')
    if inp_user == 'y':
        if player.check(player, num_cask):
            continue
        else:
            print('Игра закончена')
            sys.exit()
    if inp_user == 'n':
        if player.check(player, num_cask):
            print('Игра закончена')
            sys.exit()
        elif comp.check(comp, num_cask):
            continue

