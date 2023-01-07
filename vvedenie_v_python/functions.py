my_list = []
for i in range(6):
    number = int(input("ВВедите число: "))
    my_list.append(number)
print(my_list)
print(f'\nМаксимальное число списка: {max(my_list)}\nМинимальное число списка: {min(my_list)}\nОбщая сумма чисел в списке: {sum(my_list)}')