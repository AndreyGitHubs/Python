# 1. Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# str = '3+2*2'
# print(eval(str))

# import re
 
# actions = {
#   "^": lambda x, y: str(float(x) ** float(y)),
#   "*": lambda x, y: str(float(x) * float(y)),
#   "/": lambda x, y: str(float(x) / float(y)),
#   "+": lambda x, y: str(float(x) + float(y)),
#   "-": lambda x, y: str(float(x) - float(y))
# }
 
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
# def my_fun(expresion: str) -> str:
 
#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_fun(match.group(1)))
 
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
#     return expresion
 
# znach = '(3+2*2)+2/(2-0)'
# print(' func -  ', my_fun(znach),' - ', 'eval - ', eval(znach))



# 1. Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:
# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# Если их расположить в порядке возрастания, исключив повторения, мы получим следующую последовательность из 15 различных членов:
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
# Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?

# Перебираем все числа A в степени B
# def sequence():
#     result = set(a ** b for a in range(2, 101) for b in range(2, 101))  
#     return len(result)

# print(sequence())

