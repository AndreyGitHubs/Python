# 1. Найти НОК двух чисел

# def max_divisor(number1, number2):
#     temp = 0
#     while number2 != 0:
#         temp = number2
#         number2 = number1 % number2
#         number1 = temp
#     return number1

# def min_divisor(number1, number2):
#     return (number1 * number2) / max_divisor(number1, number2)

# num1 = 16
# num2 = 4
# nok = min_divisor(num1, num2)
# print(f"Наименьшее общее кратное {num1} и {num2} равно {nok}.")

# ---
# Вариант решения № 2
# ---

# import math
# a, b = 11, 3
# print(math.lcm(a, b))

#------
#------

# 2. Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

# def numbers(num, accuracy=0):
#     return f"{num:.{accuracy}f}"

# c = 3.141592653589793 # заданое число
# d = 8

# print(f'{numbers(c, d)} - {d} знаков после запятой')

#------
#------

# 3. Составить список простых множителей натурального числа N

# for -  обычно делитель не будет больше корня
# number //= i убираю множитель

import math

number=int(input('Введите цисло: '))

for i in range(2, int(math.sqrt(number)) + 1): 
    while (number % i == 0): 
        print(i)
        number //= i 

if (number != 1): 
    print (number)


#------
#------

# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# print(f' Отфильтрованный список:  {list(set(my_list))}')
