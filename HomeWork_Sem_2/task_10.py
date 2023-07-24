# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import choice
import os
os.system('cls')


def fill_list_with_choices(n):                 # Решка - True;  Герб - False
    n_list = []                                # создаем и рандомно заполняем список
    i = 0
    while i < n:
        n_list.append(choice([True, False]))
        i += 1
    return n_list


def count_side_of_coins(n_list):             # создание списка с кол-вом монет решкой/гербом
    c_true = 0                               
    c_false = 0
    s_list = []
    for i in range(len(n_list)):
        if n_list[i] == True:
            c_true += 1
        else:
            c_false += 1

    s_list.append(c_true)
    s_list.append(c_false)
    return s_list


def find_answer(s_list):                            # функция работает:  
                                                    # 1. Создает отд перемен для минимального кол-ва, чтоб не запутаться
    def check_word_end(s_list):                     # 2. Проверяет кол-во монет и подставляет правильное окончание, надеюсь, что правильное.
        if s_list[0] < s_list[1]:                   # 3. Выбирает вариант с наименьшим кол-вом и возвращает ответ.
            min = s_list[0]
        elif s_list[0] > s_list[1]:
            min = s_list[1]
        else:
            min = s_list[0]

        w = "монета"
        if min in (0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
            w = "монеток"
            return w
        elif min % 10 == 1:
            w = "монетку"
            return w
        elif min % 10 in (2, 3, 4):
            w = "монетки"
            return w
        else: 
            w = "монеток"
            return w

    word = check_word_end(s_list)

    if s_list[0] > s_list[1]:
        first_option = f"Переверните {s_list[1]} {word} решкой вверх"
        return first_option
    elif s_list[1] > s_list[0]:
        second_option = f"Переверните {s_list[0]} {word} гербом вверх"
        return second_option
    else:
        third_option = f"Монеток поровну. Переверните {s_list[0]} {word} решкой или гербом вверх"
        return third_option



num = int(input("Введите количество монеток на столе: "))
num_list = fill_list_with_choices(num)  # Решка - True;  Герб - False
print(num_list)

side_list = count_side_of_coins(num_list)
final_answer = find_answer(side_list)

print(f"Количество монеток решкой вверх: {side_list[0]}")
print(f"Количество монеток гербом вверх: {side_list[1]}")
print(f"Минимальное количество монеток, которые нужно перевернуть: ")
print(final_answer)



# 0 монеток     10 монеток
# 1 монетку     11 монеток
# 2 монетки     12 монеток
# 3 монетки     13 монеток
# 4 монетки     20 монеток
# 5 монеток     21 монетку
# 6 монеток     22 монетки
# 7 монеток
# 8 монеток
# 9 монеток
