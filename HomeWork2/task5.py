# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

from random import randrange

n = int(input('Введите количество чисел в списке: '))
num_list = list(range(n))
print(num_list)
new_num_list = []
while len(num_list) > 0:
        number = randrange(0, len(num_list))
        new_num_list.append(num_list.pop(number))
print(new_num_list)
