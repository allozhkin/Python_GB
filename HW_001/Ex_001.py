weekday = int(input('Введите номер дня недели от 1 до 7: '))
if weekday == 1 :
    print(f'Ваша цифра {weekday} и это будний день - понедельник')
elif weekday == 2:
    print(f'Ваша цифра {weekday} и это будний день - Вторник')
elif weekday == 3:
    print(f'Ваша цифра {weekday} и это будний день - Среда')
elif weekday == 4:
    print(f'Ваша цифра {weekday} и это будний день - Четверг')
elif weekday == 5:
    print(f'Ваша цифра {weekday} и это будний день - Пятница')
elif weekday == 6:
    print(f'Ваша цифра {weekday} и это выходной день - Суббота')
elif weekday == 7:
    print(f'Ваша цифра {weekday} и это выходной день - Воскресенье')
else:
    print('Вы ввели неверное число')