number=int(input('Введите трехзначное число: '))
first_remainder=number%10
number=number//10
second_remainder=number%10
number=number//10
third_remainder=number%10
print(f'{first_remainder} + {second_remainder} + {third_remainder} = {first_remainder+second_remainder+third_remainder}')