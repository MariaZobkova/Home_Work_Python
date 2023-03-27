# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

numb = int(input('Введите число: '))

numb_2 = int(input('Введите степень числа: '))


def power_of_number(number, power):

        if power == 0:
            return 1
        return number * power_of_number(number, power-1)


print(power_of_number(numb, numb_2))

