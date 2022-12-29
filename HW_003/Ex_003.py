#  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
#  минимальным значением дробной части элементов, отличной от 0.
import random

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    return round(max(nums) - min(nums), 2)
my_list = []
long_list = int(input("введите длинну списка: "))
for i in range(long_list):
    my_list.append(round(random.uniform(1, 10),2))
print(my_list)

print(find_diff(my_list))