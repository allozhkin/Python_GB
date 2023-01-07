# map работает с функцией и записывается так map(func, iterable)
numbers = [3,5,1,6,9,2]
print(list(map(lambda x : x**2, numbers)))
print(list(map(lambda x : str(x), numbers)))