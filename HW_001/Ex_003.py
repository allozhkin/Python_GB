flag = True
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x or y or z) != (not x and not y and not z):
                print(f'Выражение при x = {x}, y = {y}, z = {z} неверно')
if flag:
    print('При любых значениях x, y, z выражение верно')
