elements_amount = int(input('Введите количество элементов в списке: '))
elements_list = []
for i in range(elements_amount):
    elements_list.append(int(input('Введите число: ')))

print(f'Полученный список: {elements_list}')    

search_number = int(input('Введите искомое число: '))
min_difference = abs(search_number - elements_list[0])
found_number = elements_list[0]
for i in range(1, elements_amount):
    difference = abs(search_number - elements_list[i])
    if difference <= min_difference:
        min_difference = difference
        found_number = elements_list[i]
print(f'Наиболее близкое число в списке:  {found_number}')