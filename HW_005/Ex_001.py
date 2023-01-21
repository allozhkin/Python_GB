import random
# Приветствуем игроков и выбираем количество конфет

print("Добро пожаловать в игру!")
bot = "Robocop"

candy_amount = int(input("Введите количество конфет: "))
print(
    f'На столе лежит {candy_amount} конфет,\nЗа один ход можно забрать не более чем 28 конфет,')
print('Победит тот, кто заберет последние конфеты')

#  Выбераем с кем будем играть и указываем имена игроков

my_choise = int(input(
    'Нажмите "1" если вы хотите играть с ботом и "2" если хотите играть друг против друга: '))
players = []
new_players = []
if my_choise == 2:
    players_amount = int(input('Введите количество игроков: '))
    for i in range(players_amount):
        player_name = input("Введите имя игрока: ")
        players.append(player_name)
    print(f'В игре учавствуют : {players}')
    random.shuffle(players)
    print(f'Первый ход у игрока - {players[0]}')
else:
    player_name = input("Введите имя игрока: ")
    players.append(player_name)
    players.append(bot)
    print(f'В игре учавствуют : {players}')
    random.shuffle(players)
    print(f'Первый ход у игрока - {players[0]}')


# Прописываем условия 
is_winner = False
winner_name = None
while candy_amount != 0:
    for j in range(len(players)):
        print(f'На столе лежит {candy_amount} конфет')
        print(f'Ваш ход - {players[j]}')
        if players[j] == bot:
            if candy_amount <= 28:
                bot_number = candy_amount
            else:
                bot_number = random.randint(1, 29)
            print(f'{bot} выбрал число {bot_number}')
            candy_amount -= bot_number
        else:
            while True:
                try:
                    step = int(input("Введите число: "))
                    if 1 <= step <= 28:
                        break
                    else:
                        print(f"Вы ввели: {step},а надо число от 1 до 28!")
                except:
                    print("Введите пожалуйста целые числа от 1 до 28")
            candy_amount -= step
        if candy_amount <= 0:
            is_winner = True
            winner_name = players[j]
            break
print(f'Победитель: {winner_name}, Поздравляем!!')
