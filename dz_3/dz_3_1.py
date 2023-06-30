elements_amount = int(input("Введите количество элементов в списке: "))
elements_list = []

for _ in range(elements_amount):
    number = int(input("Введите число: "))
    elements_list.append(number)

print(f'Полученный список: {elements_list}')    

search_number = int(input("Введите число, которое необходимо найти: "))
counter = 0

for i in elements_list:
    if i == search_number:
        counter += 1

print(counter)