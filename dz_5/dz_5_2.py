import random

count = int(input('Введите кол-во элементов: '))

def list_generator(count):
    numbers =[]
    for _ in range(count):
        number = random.randint(1, 5)
        numbers.append(number)
    return numbers

numbers = list_generator(count)
print(numbers)

dict = {}

for i in numbers:
    element = i
    counter = 0
    for j in numbers:
        if element == j:
            counter += 1
            dict[i] = counter

print(dict)

counts = []

for item in numbers:
    counts.append(dict[item])

print(f'Максимальное количество одинаковых элементов = {max(counts)}')