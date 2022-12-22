#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на позиции с нечетным индексом.
import random
long_list = int(input("Введите длинну списка: "))
my_lst = []
for i in range(long_list):
    my_lst.append(random.randint(-10, 10))
print(f' Ваш список: {my_lst}')
sum = 0
for i in range(len(my_lst)):
    if i % 2 != 0:
        print(f'На индексе {i} стоит число {my_lst[i]}')
        sum += my_lst[i]
print(f'Сумма чисел в нечетных индексах {sum}')
