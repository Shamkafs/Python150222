# Напишите программу, которая принимает на вход 2 числа. Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

number = int(input('Введите целое число, из которого будет сформирован список от -N до N: '))
number1 = int(input('Выберите порядковый номер числа из списка: '))
number2 = int(input('Выберите ещё один порядковый номер числа из списка: '))

num_list = []
multiplication = 0
for i in range(-number, number + 1):
    num_list.append(i)
print(num_list)
if number1 <= len(num_list) and number2 <= len(num_list):
    multiplication = num_list[number1 - 1] * num_list[number2 - 1]
    print(multiplication)
else :
    print('Для одной или двух из заданных позиций нет значений в заданном списке!')
