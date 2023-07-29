# задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции
import math
import os
from decimal import Decimal, getcontext
os.system('cls')




def convert_num_rec(num, bin_n, l_convert=[], i=0):
    if num > 0:
        l_convert.insert(i, num % bin_n)
        i += 1
        return convert_num_rec(num // bin_n, bin_n, l_convert)
    else:
        return l_convert


def convert_float_part_rec(num, bin_n, num_length, list_float=[], i=0):
    if num % 1 != 0 and i < num_length:
        num *= bin_n
        list_float.append(math.floor(num))
        num = num - int(num)
        i += 1
        return convert_float_part_rec(num, bin_n, num_length, list_float, i)
    else:
        return list_float


def convert_num_loop(num, bin_n, l_convert=[]):
    while num > 0:
        l_convert.append(num % bin_n)
        num //= bin_n
    return l_convert

def convert_float_part_loop(fl_part, bin_n, n_length, list_float=[], i = 0):
    while fl_part % 1 != 0 and i < n_length:
        fl_part *= bin_n
        check_n = int(fl_part)
        list_float.append(math.floor(fl_part))
        fl_part = fl_part - check_n
        i += 1
    return list_float


def numb_check(check_num, a, b):
    if check_num == a or check_num == b:
        return check_num
    else:
        flag = True
        while flag:
            check_num = int(
                input(f"Вы ввели неверное число. Введите {a} или {b}:  "))
            if check_num == a or check_num == b:
                flag = False
        return check_num


def out_answer_check (num):
    return num % 1 == 0




number = 103.625
# number = abs(input("Введите целое число: ")
print("Введите в какую систему вы хотите перевести число:  ")
binary_num = int(input(f"Двоичная =>  <<2>> ----- Восьмиричная => <<8>>  "))
binary_num = numb_check(binary_num, 2, 8)
print("Введите метод выполнения перевода в систему исчисления.")
method_exec = int(input(
    "Для использования метода рекурсии нажмите: <<1>>.\nДля использования метода циклом нажмите:   <<2>>  "))
method_exec = numb_check(method_exec, 1, 2)

number = Decimal(str(number))
num_int = int(number)
float_part = number - num_int
num_length = len(str(number))
getcontext().prec = num_length


if binary_num == 2 and method_exec == 1:        # РЕКУРСИЯ  2
    num_2 = num_int
    list_rec_2 = convert_num_rec(num_2, 2)
    list_float_rec_2 = convert_float_part_rec(float_part, 2, num_length)
    print(f"Число {number} в двоичной системе представления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_rec_2)))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_rec_2[::-1])))
    else:
        print("".join(map(str, list_rec_2)), end=".")
        print("".join(map(str, list_float_rec_2[::-1])))

elif binary_num == 2 and method_exec == 2:          # ЦИКЛ 2
    num_2 = num_int
    list_loop_2 = convert_num_loop(num_2, 2)
    list_float_2 = convert_float_part_loop(float_part, 2, num_length)
    print(f"Число {number} в двоичной системе представления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_loop_2[::-1])))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_2)))
    else:
        print("".join(map(str, list_loop_2[::-1])), end=".")
        print("".join(map(str, list_float_2)))

elif binary_num == 8 and method_exec == 1:             # РЕКУРСИЯ  8
    num_8 = num_int
    list_rec_8 = convert_num_rec (num_8, 8)
    list_float_rec_8 = convert_float_part_rec(float_part, 8, num_length)
    print(f"Число {number} в двоичной системе представления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_rec_8)))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_rec_8[::-1])))
    else:
        print("".join(map(str, list_rec_8)), end=".")
        print("".join(map(str, list_float_rec_8[::-1])))

else:                                                    # ЦИКЛ 8
    num_8 = num_int
    list_loop_8 = convert_num_loop (num_8, 8)
    list_float_rec_8 = convert_float_part_loop(float_part, 8, num_length)
    print(f"Число {number} в двоичной системе представления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_loop_8[::-1])))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_rec_8)))
    else:
        print("".join(map(str, list_loop_8[::-1])), end=".")
        print("".join(map(str, list_float_rec_8)))










#////////////////////////////////////////////////////////////////////
# elif binary_num == 2 and method_exec == 2:


# print(f"Число {number} в двоичной системе представления: ", end="=> ")
# print("".join(map(str,list_rec_2)))


# ----------------D---O---N---E-----------------
# num_2 = num_int
# list_loop_2 = convert_num_loop (num_2, 2)
# list_float_2 = convert_float_part_loop (float_part, 2)

# print(f"Число {number} в двоичной системе представления: ", end="=> ")
# if len(list_loop_2) == 0:
#     print("0",end="")
# print("".join(map(str,list_loop_2[::-1])),end=".")
# print("".join(map(str,list_float_2)))
# -----------------------------------------------------------------------


# if binary_num == 2 and method_exec == 1:
#     num_2 = number
#     list_rec_2 = convert_num_rec (num_2, 2)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_rec_2)))


# -----------------------------------------------------------------------
# elif binary_num == 8 and method_exec == 1:
#     num_8 = number
#     list_rec_8 = convert_num_rec (num_8, 8)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_rec_8)))

# else:
#     num_8 = number
#     list_loop_8 = convert_num_loop (num_8, 8)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_loop_8[::-1])))


# number = abs(int(input("Введите целое число: ")))
# print("Введите в какую систему вы хотите перевести число:  ")
# binary_num = int(input(f"Двоичная =>  <<2>> ----- Восьмиричная => <<8>>  "))
# binary_num = numb_check (binary_num, 2, 8)
# print("Введите метод выполнения перевода в систему исчисления.")
# method_exec = int(input("Для использования метода рекурсии нажмите: <<1>>.\nДля использования метода циклом нажмите:   <<2>>  "))
# method_exec = numb_check (method_exec, 1, 2)

# if binary_num == 2 and method_exec == 1:
#     num_2 = number
#     list_rec_2 = convert_num_rec (num_2, 2)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_rec_2)))

# elif binary_num == 2 and method_exec == 2:
#     num_2 = number
#     list_loop_2 = convert_num_loop (num_2, 2)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_loop_2[::-1])))

# elif binary_num == 8 and method_exec == 1:
#     num_8 = number
#     list_rec_8 = convert_num_rec (num_8, 8)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_rec_8)))

# else:
#     num_8 = number
#     list_loop_8 = convert_num_loop (num_8, 8)
#     print(f"Число {number} в двоичной системе представления: ", end="=> ")
#     print("".join(map(str,list_loop_8[::-1])))


# ----------------------------T---E---S---T---------------------------
# i = -1
# while num > 0:
#         list_3.insert(i, num % 2)
#         i -= 1
#         num //= 2
# print(list_3)

# list_3 = (convert_num_rec(number, binary_num))
# print(list_3)


# print(f"Число {num} в двоичной системе представления: ", end="=> ")
# print("".join(map(str,list_1[::-1])))
# print(f"Число {num} в восьмеричной системе представления: ", end="=> ")
# print("".join(map(str,list_2[::-1])))


# while num_2 > 0:
#     list_1.append(num_2 % 2)
#     num_2 //= 2

# while num_8 > 0:
#     list_2.append(num_8 % 8)
#     num_8 //= 8


# def convert_num_rec (num, bin_n, l_convert = [], i = 0):
#     if num > 0:
#         l_convert.insert(i, num % bin_n)
#         i += 1
#         return convert_num_rec(num // bin_n, bin_n, l_convert)
#     else:
#         return l_convert


# list_n = convert_num_rec (18, 2)
# print(list_n)


# def num_after_fl(num):
#     if num % 1 != 0:
#         num = str(num)
#         fl_list = num.split(".")
#         num_for_r = len(fl_list[1])
#         return num_for_r


# def convert_float_part_rec (num, bin_n, num_length, list_float = [], i = 0):
#     if num % 1 != 0 and i < num_length:
#         num *= bin_n
#         if num - int(num) > 0 or num % 1 == 0:
#             list_float.append(math.floor(num))
#         else:
#             list_float.append(0)
#         num = num - int(num)
#         i += 1
#         return convert_float_part_rec (num, bin_n, num_length, list_float, i )
#     else:
#         return list_float

    # if num % 1 != 0:
    #     check_n = fl_part
    #     if int(check_n) == 1:
    #         list_float.append(1)
    #         del_num = fl_part - int(check_n)
    #         fl_part = del_num
    #     else:
    #         list_float.append(0)
    #     return convert_num_rec(num // bin_n, bin_n, list_float)
    # else:
    #     return list_float
