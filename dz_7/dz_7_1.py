def vowel_count(my_str):
    vowel_list = [ 'а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for i in my_str:
        if i in vowel_list: count +=1
    return count

poem = input('введите стих: ')
poem = poem.split()
if len(set(map(vowel_count,poem))) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')  