def personal_info(name,age,city):
    result= f'{name}, возраст = {age} год(а), проживает в городе {city}'
    return result
pers_info=personal_info('alexey', 29, 'moscow')
print(pers_info)