import math
# найти длинну окруженности с определенным радиусом
r = 100
print(f'Длинна окруженности:  {2*r*math.pi}')
# Найти площадь окруженности с определенным радиусом
print(f'Площадь окруженности: {(r**2)*math.pi}')
print(f'Площадь окруженности: {(math.pow(r, 2))*math.pi}')
# По координатам 2х точек определить расстояние между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l =math.sqrt((x1-x2)**2+(y1-y2)**2)
print(f'Расстояние между 2 точками: {l}')
# Найти Факториал числа 9
print(f'Факториал числа 9 = {math.factorial(9)}')