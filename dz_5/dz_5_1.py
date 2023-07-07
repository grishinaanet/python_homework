import random

count = int(input('Введите кол-во элементов: '))

def list_generator(count):
    numbers =[]
    for _ in range(count):
        number = random.randint(1, 100)
        numbers.append(number)
    return numbers

numbers = list_generator(count)
print(numbers)

max_number = numbers[0]

for i in numbers:
    if max_number < i:
        max_number = i

print(f'Последний локальный максимум = {numbers.index(max_number)+1}')