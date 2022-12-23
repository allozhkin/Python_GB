my_dict = {}
number = int(input('ввведите целое число: '))
for n in range(1, number+1):
    my_dict[n] = 3*n+1
print(my_dict.get(7))
