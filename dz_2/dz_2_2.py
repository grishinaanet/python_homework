sum=int(input('Введите сумму: '))
multiplicator=int(input('Введите произведение: '))
for i in range(1000):
    for j in range(1000):
        if i+j==sum and i*j==multiplicator:
            print(f"Первое число - {i}, второе число - {j}")