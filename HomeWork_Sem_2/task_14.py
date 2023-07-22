# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os
os.system('cls')


def degree_of_num_two(n):
    n_list = []          # создание списка всех значений 2^k до N
    d_list = []          # создание списка перечня всех k до N
    f_list = []          # создание объед списка (n_list и d_list) для удобства вывода в клиентском коде
    i = 0

    while 2**i <= n:
        n_list.append(2**i)
        d_list.append(i)
        i += 1

    f_list.append(n_list)
    f_list.append(d_list)
    return f_list


num = int(input("Введите число которое будет ограничивать диапозон выражения 2^х:  "))
fin_list = degree_of_num_two(num)
print(f"Все степени двойки, не превосходящие число {num}:", end="  ")
print(", ".join(map(str,fin_list[0])))
print(f"Перечень степеней двойки, не превосходящих число {num}:", end="  ")
print(", ".join(map(str,fin_list[1])))

