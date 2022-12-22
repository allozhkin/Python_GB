# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
my_list = []
list_long = int(input("ВВедите длинну списка: "))
for i in range(list_long):
    my_list.append(random.randint(1, 10))
print(f'Ваш список: {my_list}')

for i in range(len(my_list) // 2):
    if len(my_list) % 2 ==1 and i == len(my_list) // 2:
        print("no")
    else:
        print(f"Произведение чисел {my_list[i]} и {my_list[len(my_list) - 1 - i]} ровняется {my_list[i] * my_list[len(my_list) - 1 - i]}")