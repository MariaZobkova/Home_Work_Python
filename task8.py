# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_length = int(input('Введите размер одной стороны шоколадки '))

chocolate_height = int(input('Введите размер другой стороны шоколадки '))

number_of_slices = int(input('Введите количество долек шоколадки '))

if (number_of_slices % chocolate_length == 0 or number_of_slices % chocolate_height == 0) and (chocolate_length * chocolate_height > number_of_slices):
    print('yes')
else:
    print('no')
