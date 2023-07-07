import random

count = int(input('Введите кол-во элементов: '))

def list_generator(count):
    numbers =[]
    for _ in range(count):
        number = random.randint(1, 20)
        numbers.append(number)
    return numbers

numbers = list_generator(count)

print('Сгенерированный список: ', numbers)

dict = {}

for i in numbers:
    element = i
    counter = 0
    for j in numbers:
        if element == j:
            counter += 1
            dict[i] = counter

print(dict)

for (key, value) in dict.items():
    print("Значений", key, "всего", value, "штук(и)")