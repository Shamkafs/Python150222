#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите номер дня недели, где 1 - понедельник и тд: '))

if number < 1 or number > 7:
    print('Введён некорректный номер дня недели')
elif number < 6:
    print('Не является выходным днём')
else:
    print('Является выходным днём')
