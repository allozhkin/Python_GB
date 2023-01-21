total_person = int(input("введите колличество участников: "))
my_list = []
i = total_person
for i in range(total_person):
    name = input(f"кто занял {i+1} место? ").upper()
    my_list.append(name)
print(f'В соревнованиях учавствовали: {my_list}')
print(f'Поздравляем победителей: {my_list[:3]}')