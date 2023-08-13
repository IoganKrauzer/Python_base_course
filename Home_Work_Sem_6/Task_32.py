# (ИЗ ПРЕЗЕНТАЦИИ) Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# (С САЙТА В ПРАКТИЧЕСКИХ ЗАДАНИЯХ) Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import randint
import os
os.system('cls')




def create_list(_num):
    _generate_list = [None] * _num
    for i in range(len(_generate_list)):
        _generate_list[i] = randint(-250, 250)
    return _generate_list


def find_indx_in_interval(_generated_list, _start_point, _end_point):
    def print_dict(_dic_interv):
        for key, value in _dic_interv.items():
            print(key, "-----", value)

    _dic_interval_num = {}
    for i in range(len(_generated_list)):
        if (_generated_list[i] > _start_point and _generated_list[i] < _end_point or 
            _generated_list[i] < _start_point and _generated_list[i] > _end_point):
            _dic_interval_num[f"Индекс: {i}; "] = f" Значение => {_generated_list[i]}"

    if len(_dic_interval_num) >= 1:
        print_dict(_dic_interval_num)
    else:
        print("В пределах заданного интервала значений нет")




len_number = int(input("Введите длинну списка: "))
start_inter_point = int(input("Введите начало интервала: "))
end_inter_point = int(input("Введите границу интервала: "))
generated_list = create_list(len_number)
print("Сненерированный список: ", generated_list)
find_indx_in_interval(generated_list, start_inter_point, end_inter_point)
