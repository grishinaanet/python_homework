import random

count = int(input('Введите кол-во элементов: '))

def list_generator(count):
    numbers =[]
    for _ in range(count):
        number = random.randint(1, 20)
        numbers.append(number)
    return numbers

numbers = list_generator(count)

start_range = int(input('Введите число начала диапазона: '))
end_range = int(input('Введите число окончания диапазона: '))

print('Сгенерированный список: ', numbers)

range_numbers = []

for i in numbers:
    if start_range < i and i < end_range:
        range_numbers.append(i)

print('Элементы сгенерированного списка, которые удовлетворяют заданному диапазону: ', range_numbers)