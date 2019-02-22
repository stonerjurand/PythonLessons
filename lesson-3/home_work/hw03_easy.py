# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    leftpart = str(int(number))
    number = list(str(number))
    number.remove('.')
    while len(number) > ndigits:
        if int(number[-1]) >= 5:
            number[-2] = str(int(number[-2]) + 1)
            number = number[:-1]
        else:
            number = number[:-1]
    rvr = number[::-1]
    for index, digit in enumerate(rvr):
        if int(digit) == 10:
            rvr[index] = digit[1]
            rvr[index + 1] = str(int(rvr[index + 1]) + 1)
    number = rvr[::-1]
    if ndigits == len(leftpart):
        return int(''.join(number))
    else:
        number.insert(len(leftpart), '.')
        return float(''.join(number))


# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))

#print("Test1")
print(f'Mine: {my_round(2.1234567, 5)}')
print(f'Built-in: {round(2.1234567, 5)}')
print(f'Mine: {my_round(2.1999967, 5)}')
print(f'Built-in: {round(2.1999967, 5)}')
print(f'Mine: {my_round(2.9999967, 5)}')
print(f'Built-in: {round(2.9999967, 5)}')
print("Test2")
print(f'Mine: {my_round(-2.1234567, 5)}')
print(f'Built-in: {round(-2.1234567, 5)}')
print(f'Mine: {my_round(-2.1999967, 5)}')
print(f'Built-in: {round(-2.1999967, 5)}')
print(f'Mine: {my_round(-2.9999967, 5)}')
print(f'Built-in: {round(-2.9999967, 5)}')
print("Test3")
print(f'Mine: {my_round(-2.1234567, 0)}')
print(f'Built-in: {round(-2.1234567, 0)}')
print(f'Mine: {my_round(-2.1999967, 0)}')
print(f'Built-in: {round(-2.1999967, 0)}')
print(f'Mine: {my_round(-2.9999967, 0)}')
print(f'Built-in: {round(-2.9999967, 0)}')
print("Test4")
print(f'Mine: {my_round(2.1234567, -5)}')
print(f'Built-in: {round(2.1234567, -5)}')
print(f'Mine: {my_round(2.1999967, -5)}')
print(f'Built-in: {round(2.1999967, -5)}')
print(f'Mine: {my_round(2.9999967, -5)}')
print(f'Built-in: {round(2.9999967, -5)}')
print("Test5")
print(f'Mine: {my_round(-2.1234567, -5)}')
print(f'Built-in: {round(-2.1234567, -5)}')
print(f'Mine: {my_round(-2.1999967, -5)}')
print(f'Built-in: {round(-2.1999967, -5)}')
print(f'Mine: {my_round(-2.9999967, -5)}')
print(f'Built-in: {round(-2.9999967, -5)}')
print("Test6")
print(f'Mine: {my_round(-253002.1234567, -5)}')
print(f'Built-in: {round(-253002.1234567, -5)}')
print(f'Mine: {my_round(-2.1999967, -5)}')
print(f'Built-in: {round(-2.1999967, -5)}')
print(f'Mine: {my_round(-2.9999967, -5)}')
print(f'Built-in: {round(-2.9999967, -5)}')

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky_ticket(ticket_number):
#     number = list(str(ticket_number))
#     listnumber = list(map(lambda x: int(x), number))
#     if len(number) == 6:
#         if sum(listnumber[:3]) == sum(listnumber[3:]):
#             return 'Поздравляем! У Вас счастливый билет!'
#         else:
#             return 'Возможно в следующий раз Вам повезёт!'
#     else:
#         return 'Введите корректный номер билета, состоящий из 6 цифр'
#
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
