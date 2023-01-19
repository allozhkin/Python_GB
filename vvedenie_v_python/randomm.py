from random import randint, choice, sample, shuffle

# 1. Загадать случайное число от 0 до 100
print(randint(0, 100))
# 2. Выбрать победителя лотерее из списка
players = ["max", 'leo', 'kate', 'ron', 'bil']
print(choice(players))
# 3. Выбрать трех победителей из списка
print(sample(players,3))
# 4. Перемешать карты в
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(f'Ваша колода :{cards}')
shuffle(cards)
print(f'Перемешанная колода: {cards}')
