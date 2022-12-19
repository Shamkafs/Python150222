# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num_list = []
n = int(input('Введите длину списка: '))
sum = 0
for i in range(1, n + 1):
    num_list.append((1 + 1/i) ** i)
print(num_list)
for number in num_list:
    sum += number
print(round(sum, 3))
