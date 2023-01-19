# # #  Реализуйте алгоритм перемешивания списка.
# import random
# import math
# # # Было
# my_list = []
# for _ in range(10):
#     my_list.append(round(random.randint(0, 10)))
# print(my_list)

# # Стало
# my_list = [x for x in range(10)]
# print(my_list)
# random.shuffle(my_list)
# print(my_list)

# #  Задайте список из нескольких чисел.
# # Было
# long_list = int(input("Введите длинну списка: "))
# my_lst = []
# for i in range(long_list):
#     my_lst.append(random.randint(-10, 10))
# print(f' Ваш список: {my_lst}')
# sum = 0
# for i in range(len(my_lst)):
#     if i % 2 != 0:
#         print(f'На индексе {i} стоит число {my_lst[i]}')
#         sum += my_lst[i]
# print(f'Сумма чисел в нечетных индексах {sum}')
# # Стало
# long_list = int(input("Введите длинну списка: "))
# my_lst = [random.randint(-10, 10) for i in range(long_list)]
# print(f' Ваш список: {my_lst}')

# numbers = [my_lst[i] for i in range(len(my_lst)) if i %2 != 0]
# print(f'Числа на не четных индексах: {numbers}')
# print(f'Сумма чисел стоящих на не четных индексах: {sum(numbers)}')
