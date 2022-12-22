# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.

n = int(input("Введите целое число : "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial, end=' ')
