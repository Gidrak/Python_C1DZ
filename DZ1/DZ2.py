# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# Примеры:

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

Gidrak = int(float(input("Введите число: "))*10)%10

print(Gidrak)