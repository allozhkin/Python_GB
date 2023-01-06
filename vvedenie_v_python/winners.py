total_person = int(input("введите колличество участников: "))
my_list = []
i = total_person
while i > 0:
    name = input(f"кто занял {i} место? ").upper()
    my_list.append(name)
    i -= 1
print(f'В соревнованиях учавствовали: {sorted(my_list)}')
my_list.reverse()
print(f'Поздравляем победителей: {my_list[:3]}')
