# 1. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# def countfromN(num):
#     count = ''
#     index = 1
#     for i in list(range(num)):
#         count = count + str(index) + ' '
#         index *= -3
#     print(count)

# countfromN(5)

#------
#------

# 2. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# one = "123123123"
# two = "123"
# free = 0
# for i in range(len(one) - len(two) + 1):
#     if one[i:i + len(two)] == two:
#         free += 1
# print(free)

#------
#------

# 3. Подсчитать сумму цифр в вещественном числе.

# def summa(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum

# print(summa(99887745121))

# 4. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# print('введите длинну')
# num = int(input())
# print(' ')
# one = 1
# for i in range(1, num + 1):
#     one = one * i
#     print(one)

# Задача из доп. 1. Написать функцию write_in_morse, которая принимает строку на английском языке и 
# возвращает ее перевод на символьный язык Морзе. Ввод не должен зависеть от регистра.


# char_to_dots = {'a': '.—', 'b': '—...', 'c': '—.—.', 'd': '—..', 'e': '.', 'f': '..—.', 'g': '——.', 'h': '....', 'i': '..', 'j': '.———', 'k': '—.—', 'l': '.—..', 'm': '——', 'n': '—.', 'o': '———', 'p': '.——.', 'q': '——.—', 'r': '.—.', 's': '...', 't': '—', 'u': '..—', 'v': '...—', 'w': '.——', 'x': '—..—', 'y': '—.——', 'z': '——..', 
#                 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
#                 ' ': ' ', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}
 
# a = input()
# a = a.lower()
# g = []
# j=0
 
# for i in a:
#     k = char_to_dots.get(i,'\t')
#     if k != '\t':
#         j = k+" "
#         g.append(j)
#     else:
#         j ='\t'
#         g.append(j)
# print("".join(g))