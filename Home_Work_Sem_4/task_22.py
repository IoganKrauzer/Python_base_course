# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random
import os
os.system('cls')


def fill_list(list_len):                   # Создаем и заполняем список сгенерированными числами
    l_fill = [None] * list_len
    for i in range(len(l_fill)):
        l_fill[i] = random.randint(1, 21)
    return l_fill


def set_answer(s_l):                       # Сортировка "Выбором"
    for i in range(len(s_l) - 1):
        min = i + 1
        for j in range(i + 1, len(s_l)):
            if s_l[min] > s_l[j]:
                min = j
        if s_l[i] > s_l[min]:
            temp = s_l[i]
            s_l[i] = s_l[min]
            s_l[min] = temp
    return s_l


# l_1_len = 11
# l_2_len = 6
# l_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
# l_2 = [3, 6, 9, 12, 15, 18]


l_1_len = int(input("Введите длинну первого набора: "))
l_2_len = int(input("Введите длинну второго набора: "))

l_1 = fill_list(l_1_len)
l_2 = fill_list(l_2_len)

set_list = list(set(l_1).intersection(set(l_2)))
print(f"Первый набор: {l_1}")
print(f"Второй набор: {l_2}")
print(f"Числа встречаются в обоих наборах: {set_answer (set_list)}")





