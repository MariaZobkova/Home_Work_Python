# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import math
import random

size = int(input('Введите размер списка: '))

my_list = [random.randint(1, 20) for i in range(size)]
print(my_list)

num = int(input('Введите число: '))

for item in my_list:
    if item == num:
        print(f'Число {num} присутствует в списке')
        break
else:
    count_list = [abs(my_list[_] - num) for _ in range(size)] # вспомогательный массив состоящий из разности числа в осн массиве и искомого значения num по модулю
    # print(count_list)
    print(my_list[count_list.index(min(count_list))])





