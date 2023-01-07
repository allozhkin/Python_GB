player_name = input('ВВедите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 25,
    'armor': 2
}
enemy_name = input('Введите имя соперника: ')
enemy = {
    'name': enemy_name,
    'health': 86,
    'damage': 31,
    'armor': 1.2
}


def get_armor(damage, armor):
    return damage/armor


def attack(unit1, unit2):
    damage = get_armor(unit1['damage'], unit2['armor'])
    unit2['health'] -= damage


print([player])
print(attack(enemy, player))
print(player)
