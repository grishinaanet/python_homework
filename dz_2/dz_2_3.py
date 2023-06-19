N = int(input("Введите предельное число: ")) 

k = 0
f = 0

while N > f and 2 ** k <= N:
    f = 2 ** k
    print(f)
    k += 1