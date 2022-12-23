#   Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения
equation = '1*x**2-4*x+4'.replace(' ', '')
mid_split = equation.replace('*', '').split('x')
c = int(mid_split[2])
a = int(mid_split[0])
b = int(mid_split[1].replace('2', ''))
print(f'наш список : {a, b, c}')
d = b**2-4*a*c
if d > 0:
    x1 = (-b+d**0.5) / (2*a)
    x2 = (-b-d**0.5) / (2*a)
    print(f'x1 = {x1},x2 = {x2}')
elif d == 0:
    x = (-b)/(2*a)
    print(f'x = {x}')
else:
    print('крпней нет')
