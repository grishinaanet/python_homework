n = int(input("Введите количество монеток: "))

tail = 0
eagle = 0

while n != 0:
    a = int(input("Какая сторона у монетки? Если решка - 0, орел - 1: "))
    if a == 0:
        tail += 1
    else:
        eagle += 1 
    n -= 1

if tail > eagle:
    print(eagle)
else:
    print(tail)