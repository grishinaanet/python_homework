massive = []

first_number=int(input('Введите первое число: '))
count_values=int(input('Введите количество чисел: '))
n = 1

def arith_progress(first_number, n, count_values):
    if n > count_values:
        return massive
    massive.append(first_number + (n-1) * count_values)
    return arith_progress(first_number, n+1, count_values)

print(arith_progress(first_number, n, count_values))