# 1. Напишите программу, удаляющую из текста все слова содержащие "абв". 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

# list_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
# print(f'Изначальный текст : {list_text}')

# def del_text(text):
#    text = list(filter(lambda x: x.lower().find('абв') == -1, text.split()))
#    return " ".join(text)

# list_text = del_text(list_text)
# print(f'Результат : {list_text}')

# ---

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

# from tkinter import *
# import random
# root = Tk()
# root.title('Criss-cross')
# game_run = True
# field = []
# cross_count = 0

# # Новая игра
# def new_game():
#     for row in range(3):
#         for col in range(3):
#             field[row][col]['text'] = ' '
#             field[row][col]['background'] = 'lavender'
#     global game_run
#     game_run = True
#     global cross_count
#     cross_count = 0

# # Проверка нажатий
# def click(row, col):
#     if game_run and field[row][col]['text'] == ' ':
#         field[row][col]['text'] = '+'
#         global cross_count
#         cross_count += 1
#         verify_win('+')
#         if game_run and cross_count < 5:
#             computer()
#             verify_win('-')

# # Проверка победы
# def verify_win(smb):
#     for n in range(3):
#         verify_line(field[n][0], field[n][1], field[n][2], smb)
#         verify_line(field[0][n], field[1][n], field[2][n], smb)
#     verify_line(field[0][0], field[1][1], field[2][2], smb)
#     verify_line(field[2][0], field[1][1], field[0][2], smb)

# def verify_line(a1,a2,a3,smb):
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
#         a1['background'] = a2['background'] = a3['background'] = 'pink'
#         global game_run
#         game_run = False

# # Действия аппанента
# def comp_win(a1,a2,a3,smb):
#     res = False
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
#         a3['text'] = '-'
#         res = True
#     if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
#         a2['text'] = '-'
#         res = True
#     if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
#         a1['text'] = '-'
#         res = True
#     return res

# def computer():
#     for n in range(3):
#         if comp_win(field[n][0], field[n][1], field[n][2], '-'):
#             return
#         if comp_win(field[0][n], field[1][n], field[2][n], '-'):
#             return
#     if comp_win(field[0][0], field[1][1], field[2][2], '-'):
#         return
#     if comp_win(field[2][0], field[1][1], field[0][2], '-'):
#         return
#     for n in range(3):
#         if comp_win(field[n][0], field[n][1], field[n][2], '+'):
#             return
#         if comp_win(field[0][n], field[1][n], field[2][n], '+'):
#             return
#     if comp_win(field[0][0], field[1][1], field[2][2], '+'):
#         return
#     if comp_win(field[2][0], field[1][1], field[0][2], '+'):
#         return
#     while True:
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
#         if field[row][col]['text'] == ' ':
#             field[row][col]['text'] = '-'
#             break

# # графический интерфейс
# for row in range(3):
#     line = []
#     for col in range(3):
#         button = Button(root, text=' ', width=4, height=2, 
#                         font=('Verdana', 20, 'bold'),
#                         background='lavender',
#                         command=lambda row=row, col=col: click(row,col))
#         button.grid(row=row, column=col, sticky='nsew')
#         line.append(button)
#     field.append(line)
# new_button = Button(root, text='new game', command=new_game)
# new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
# root.mainloop()

# 3 Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. 
# Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. 
# Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. 
# И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, 
# жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. 
# Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, 
# короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. 
# Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».

# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну, эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ.... Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту... ээээ... яму. Хлеба купил».

# def filter_text(file_path: str) -> None:
#     ignore_text = ['короче', 'короче говоря', 'говоря', 'кажется', 'ну', 'эээ', 'в общем', 'как бы', 'эээээ', 'ясен пень', 'кстати', 'ээээ']

#     with open(file_path, "r", encoding='utf-8') as file:
#         registr = file.readline().lower()
#         print(registr)
#         for ignore in ignore_text:
#             registr = registr.replace(', ' + ignore, '')
#         for ignore in ignore_text:
#             registr = registr.replace(' ' + ignore, '')
#         for ignore in ignore_text:
#            registr = registr.replace(ignore, '')

#     while registr[1] == ',' or registr[1] == ' ' or registr[1] == '...':
#         registr = registr[1:]

#     registr = '«' + registr

#     with open(file_path, "w", encoding='utf-8') as file:
#         file.write(registr)

# filter_text('text.txt')

