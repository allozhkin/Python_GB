num = int(input("введите целое число: "))
new_list = []
for i in range(1, num+1):
    new_list.append(round((1+1/i)**i, 2))
print(*new_list, sep=', ')
print(sum(new_list))