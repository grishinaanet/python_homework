length=int(input('Введите длину шоколадки: '))
width=int(input('Введите ширину шоколадки: '))
number=int(input('Сколько тебе кусочков отломить?: '))
if number%length==0 or number%width==0:
    print("Держи свой шоколадный прямоугольник!")
else: print("Прямоугольник не получается(((")