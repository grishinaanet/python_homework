import random

count = int(input('Введите кол-во элементов: '))

def list_generator(count):
    numbers =[]
    for _ in range(count):
        number = random.randint(1, 9)
        numbers.append(number)
    return numbers

numbers = list_generator(count)
print(numbers)
undo = list(set(numbers))
print(undo[-2])