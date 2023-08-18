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
    def total_matches(_value):
        return _value[0] + _value[1] + _value[2]
        
    for key, value in _d.items():
        print(f"{key} : {total_matches(value)}", value[0], value[1], value[2], value[0] * 3 + value[1])




match_num = int(input("Введите кол-во матчей: "))
d = create_d_with_results(match_num)
print_total_result(d)








