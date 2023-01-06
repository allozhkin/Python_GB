# загадали число
import random
number = random.randint(1, 100)
print(number)
# Определили уровень игры
user_number = None
count = 0
levels = {1: 10, 2: 6, 3: 3}
# Выбор уровня пользователем
max_count = int(input('Введите уровень сложности вашей игры от 1 до 3: '))
level = levels[max_count]
if max_count == 1:
    print(f'Вы выбрали {max_count} уровень,\nу вас есть аж 10 попыток')
elif max_count == 2:
    print(f'Вы выбрали {max_count} уровень,\nу вас есть целых 6 попыток')
elif max_count == 3:
    print(
        f'Вы выбрали {max_count} уровень,\nу вас есть всего 3 попытки\nудачи!')
# выбираем количество пользователей
user_count = int(input('Введите количество пользователей: '))
user_names = []
for i in range(user_count):
    user_name = input(f'Введите имя {i+1} пользователя: ')
    user_names.append(user_name)
print(user_names)
# Прописываем условие
is_winner = False
winner_name = None
while not is_winner:
    count += 1
    if count > level:
        print('Все игроки проиграли...')
        break
    print()
    print(f'Попытка № {count}')
    # Устанавливаем  очередь
    for user in user_names:
        print(f'Ход пользователя {user} ')
# Первая попытка
        user_number = int(input("Введите число от 1 до 100 - "))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif user_number > number:
            print("Ваше число больше загаданного.")
        else:
            print("Ваше число меньше загаданного.")
else:
    print(f"Ура,{winner_name} ты угадал!)")
