# 1. 3.  Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
#  Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# def increasing(my_list):
#     list = [my_list[0]]
#     for i in my_list:
#         if i > max(list):
#             list.append(i)
#     return list
    
# print(increasing(my_list))

# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

# from random import randint
# my_set = {randint(-10, 10) for i in range(10)}

# print(my_set)

# with open('readme.txt', 'w') as data:
#     data.write(str(my_set))

# my_list=list(my_set)
# my_list.sort()
# print(my_list)

# with open('readme.txt', 'a') as data:
#     data.write(str(my_list))




