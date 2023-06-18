number=int(input('Введите номер билета: '))
first_number=number%10
number=number//10
second_number=number%10
number=number//10
third_number=number%10
number=number//10
forth_number=number%10
number=number//10
fifth_number=number%10
number=number//10
sixth_number=number%10
if first_number+second_number+third_number==forth_number+fifth_number+sixth_number:
    print("Билет счастливый!")
else: print("В этот раз не повезло:(")