# 1. Найти сумму чисел списка стоящих на нечетной позиции
#    Пример:[1,2,3,4] -> 4

# list = [int(input('Введите элемент списка: ')) for i in range(int(input('Введите длину списка: ')))]
# list = [1,2,3,4,5,6,7,8,9]
# composition = 1
# for i in list:
#     composition *= i

from random import randint
list = [randint(-10, 10) for i in range(10)]

total = 0
for i in list:
    if i % 2 != 0:
        total += i

print(f'Весь список: {list}')
print(f'Сумма элементов списка равна: {sum(list)}')
#print(f'Произведение элементов списка: {lst * i for i in list}')
print(f'Сумма чисел на нечетных позициях: {total}')

#------
#------

# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#    Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# from random import randint
# import math

# def get_num(n, first, last):
#     return [randint(first, last) for i in range(n)]

# def mult_pairs(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# kol = 6
# frst = 1
# last = 10

# list = get_num(kol, frst, last)
# print(' ')
# print(f'Перваначальный список чисел: {list}')
# print(f'Произведение пар чисел: {mult_pairs(list)}')

#------
#------

# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением 
#    дробной части    элементов. 
#    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform

# def get_real_nums (kol, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(kol)]

# def find_diff(mynums):
#     num = [round(x - int(x), 2) for x in (mynums)]
#     return max(num) - min(num)

# kol = 5
# first = 1
# last = 10
# mynums = get_real_nums(kol, first, last)

# print(' ')
# print (f'Вывод чисел: {mynums}')
# print(f'Разница между макс. и мин. значением дробной части: {find_diff(mynums)}')

#------
#------

# 4. Написать программу преобразования десятичного числа в двоичное

# print(' ') 
# print("введите десятичное число для преобразование в двоичное")
# num = int(input())
# index = ''

# while num > 0:
#     index = str(num % 2) + index
#     num = num // 2
 
# print(index)

#------
#------

# Доп. 3. Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
#         Начиная с 1 и 2, первые 10 элементов будут:
#         1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#         Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

# fib_seq = {}

# def fib_iterative(n):
#     if n in fib_seq.keys():
#         return fib_seq[n]
#     fib1, fib2, x = 0, 1, n
#     while x > 0:
#         fib1, fib2 = fib2, fib1 + fib2
#         x -= 1
#     fib_seq[n] = fib1
#     return fib1

# summ = 0
# last_fib = i = 0
# while last_fib <= 4000000:
#     last_fib = fib_iterative(i)
#     if last_fib % 2 == 0:
#         summ += last_fib
#     i += 1

# print(summ)
# print(fib_seq)


	

