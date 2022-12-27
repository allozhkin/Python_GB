n = int(input('Введите число: '))
print(f'Из десятичного числа {n}, ')
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(f'получается двоичное {b}')
