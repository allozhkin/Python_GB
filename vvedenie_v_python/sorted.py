numbers = [1, 11, 3, 7, 5, 9]
print(sorted(numbers))  # сортирует по возрастанию
print(sorted(numbers, reverse=True))   # сортирует по убыванию


# Сортирует строки по алфавиту
names = ['kate', 'jon', 'alex', 'ron']
print(sorted(names))

# Сортировка по ключам
cities = [('Moscow', 1000), ('Vegas', 500), ('Antverpen', 2000)]
print(sorted(cities))


def counts(citie):
    return citie[1]


print(sorted(cities, key=counts))
print(sorted(cities, key=lambda city: city[1]))
