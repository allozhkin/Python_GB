# list comprehension
my_list = [i for i in range(10)]
print(my_list)


# map работает с функцией и последовательностью, применяет функцию  
string = '1 2 3 5 54 4567900 02 4 '
string = string.split()
print(string)
# for i in range(len(string)):
#     string[i] = int(string[i])
string = list(map(int, string))
print(string)

# filter Работает сс функцией и последовательностью, пробегается по всему списку
string = list(filter(lambda x : x%2, string ))  # lambda небольшая функция
print(string)

# enumerate
for i, item in enumerate(string):
    print(i, item)

# zip создает кортежи и склеивает в них списки
nums = '1 2 3 4 5 6 7'
letters = 'a b c d e f g'
nums=nums.split()
letters = letters.split()
new_list = list(zip(nums, letters))
print(new_list)