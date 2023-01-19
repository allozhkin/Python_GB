nums1 = '3+3*9'  # = 30
nums2 = '9*2-7'  # = 11
nums3 = '5-20/2'  # = -5
nums4 = '6/3-8'  # = -6

numbers = nums1.replace('+', ' + ').replace('-',
                                            ' - ').replace('*', ' * ').replace('/', ' / ').split()
print(numbers)
summ = 0
for i in range(len(numbers)):
    if numbers[i] == '*':
        numbers[i-1] = int(numbers[i-1])*int(numbers[i+1])
    if numbers[i] == '/':
        numbers[i-1] = int(numbers[i-1])/int(numbers[i+1])
numbers.pop(), numbers.pop()
for i in range(len(numbers)):
    if numbers[i] == '+':
        numbers[i-1] = int(numbers[i-1])+int(numbers[i+1])
    if numbers[i] == '-':
        numbers[i-1] = int(numbers[i-1])-int(numbers[i+1])
numbers.pop(), numbers.pop()
print(numbers)
