first_elements_amount = int(input("Введите количество элементов в первом списке: "))
second_elements_amount = int(input("Введите количество элементов во втором списке: "))

first_elements_list = []
second_elements_list = []

for _ in range(first_elements_amount):
    number = int(input("Введите число в первый список: "))
    first_elements_list.append(number)

for _ in range(second_elements_amount):
    number = int(input("Введите число во второй список: "))
    second_elements_list.append(number)    

print(f'Первый список: {first_elements_list}') 
print(f'Второй список: {second_elements_list}') 

first_set = set(first_elements_list)
second_set = set(second_elements_list)

print(f'Результат: {first_set.intersection(second_set)}')