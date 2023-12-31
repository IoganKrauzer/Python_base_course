# Задача FOOTBALL необязательная
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и 
# выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.

# Пример входа:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Выход будет:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

import os
os.system('cls')




def create_d_with_results(m_num):
    _d = {}
    for _ in range (m_num):
        list_help = input().split(";")
        _d.setdefault(list_help[0], [0, 0, 0]), _d.setdefault(list_help[2], [0, 0, 0])  #  победы, ничьи, поражение
        if int(list_help[1]) > int(list_help[3]):
            _d[list_help[0]][0] += 1
            _d[list_help[2]][2] += 1
        elif int(list_help[1]) < int(list_help[3]): 
            _d[list_help[0]][2] += 1
            _d[list_help[2]][0] += 1
        elif int(list_help[1]) == int(list_help[3]): 
            _d[list_help[0]][1] += 1
            _d[list_help[2]][1] += 1
    return _d


def print_total_result(_d):
    for key, value in d.items():
        print(f"{key} : {sum(value)}", value[0], value[1], value[2], value[0] * 3 + value[1])




match_num = int(input("Введите кол-во матчей: "))
d = create_d_with_results(match_num)
print_total_result(d)







































# def print_table(_total_table):
#     for item, value in _total_table.items():
#         print(item, value)


# def dic_for_input():
#     _input_dic = {}
#     flag = True
#     count_helper = int(input("Введите кол-во матчей: "))
#     while flag:
#         list_help_1 = []
#         list_help_3 = []
#         list_help_1.append(input("Введите наименование первой команды: "))
#         list_help_1.append(int(input("Введите наименование кол-во забитых голов: ")))
#         list_help_1.append(input("Введите наименование второй команды: "))
#         list_help_1.append(int(input("Введите наименование кол-во забитых голов: ")))
#         # tupple_1 = tuple(list_help_1[:2])
#         # tupple_2 = tuple(list_help_1[2:])
#         # list_help_3.append(tupple_1)
#         # list_help_3.append(tupple_2)
#         # print(list_help_3)
#         _input_dic[count_helper] = list_help_1
#         count_helper -= 1
#         if count_helper == 0:
#             flag = False

#     return _input_dic


# def match_report(_total_table, _input_dict ):
#     for k, v in _input_dict:
#         for i in range (len(v)):     
#             num_1 = int(v[1])
#             num_2 = int(v[3])
#             if num_1 > num_2:
#                 num_3 = 3
#                 num_4 = 0
#             elif num_1 < num_2:
#                 num_3 = 0
#                 num_4 = 3
#             else:
#                 num_3 = 1
        

   





# total_table = {}
# total_table["Наименование команды"] = ["Всего игр", "Побед", "Ничьих", "Поражений", "Всего очков"]
# total_table["Спартак             "] = [None] * 5
# total_table["Локомотив           "] = [None] * 5
# total_table["Зенит               "] = [None] * 5
# print_table(total_table)
# input_dict = dic_for_input()
# print(input_dict)