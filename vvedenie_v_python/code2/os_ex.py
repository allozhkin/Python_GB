import os
# os name
print(os.name)
# текущая рабочая дерриктория

print(os.getcwd())
# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
# Создаем папку по новому пути
os.mkdir(new_path)