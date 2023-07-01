bush_amount = int(input('Введите количество кустов на грядке (кустов должно быть больше двух!): '))
if bush_amount < 3: print('Кустов должно быть больше двух!')
else:
    bush_list = []
    for i in range(bush_amount):
        bush_list.append(int(input('Введите количество ягод (продоносность): ')))

    first_kit = bush_list[0] + bush_list[1] + bush_list[bush_amount-1]
    last_kit = bush_list[0] + bush_list[bush_amount-2] + bush_list[bush_amount-1]
    max_kit = 0
    if first_kit > last_kit:
        max_kit = first_kit
    else: max_kit = last_kit    
    for i in range(1, bush_amount-1):
        if max_kit < bush_list[i] + bush_list[i-1] + bush_list[i+1]:
            max_kit = bush_list[i] + bush_list[i-1] + bush_list[i+1]
    print(max_kit)