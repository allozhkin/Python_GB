contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
print(contacts)

name = input()
for i in contacts:
    if name in i:
        print(f'{str(i[0])} is {str(i[1])}')
        break
    else:
        print('Not Found')

