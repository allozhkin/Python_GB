text = ['fhf', 'sgj', 'jrr']
search = 'sgj'
count = 0
stop = 2
for i in range(len(text)):
    if text[i] == search:
            count+=1
            if count == stop:
                print(f'искомое встречается на индексе {i}')
if count < stop:
    print('-1')