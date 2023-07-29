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




def convert_num_rec(num: int, bin_n: int, l_convert: list = [], i: int = 0) -> list:  
    if num > 0:                                                                   
        l_convert.insert(i, num % bin_n)                                  # Для перевода числа до точки в заданную
        i += 1                                                            # систему исчисления. Через рекурсию
        return convert_num_rec(num // bin_n, bin_n, l_convert)
    else:
        return l_convert


def convert_float_part_rec(num: Decimal, bin_n: int, num_length: int, list_float: list = [], i: int = 0) -> list:
    if num % 1 != 0 and i < num_length:
        num *= bin_n                                                       # Для перевода числа после точки в заданную
        list_float.append(math.floor(num))                                 # систему исчисления. Через рекурсию
        num = num - int(num)
        i += 1
        return convert_float_part_rec(num, bin_n, num_length, list_float, i)
    else:
        return list_float


def convert_num_loop(num: int, bin_n: int, l_convert: list =[]) -> list:
    while num > 0:                                                        # Для перевода числа до точки в заданную
        l_convert.append(num % bin_n)                                     # систему исчисления. Через цикл
        num //= bin_n
    return l_convert


def convert_float_part_loop(fl_part: Decimal, bin_n: int, n_length: int, list_float: float=[], i: int = 0) -> list:
    while fl_part % 1 != 0 and i < n_length:
        fl_part *= bin_n                                                  # Для перевода числа после точки в заданную
        check_n: int = int(fl_part)                                       # систему исчисления. Через цикл
        list_float.append(math.floor(fl_part))
        fl_part = fl_part - check_n
        i += 1
    return list_float


def numb_check(check_num, a : int, b: int) -> int:                        # Для проверки ввода пользователем
    if check_num == a or check_num == b:                                  # в переменных:
        return check_num                                                  # --- binary_num
    else:                                                                 # --- method_exec
        flag = True
        while flag:
            check_num = int(
                input(f"Вы ввели неверное число. Введите {a} или {b}:  "))
            if check_num == a or check_num == b:
                flag = False
        return check_num


def out_answer_check (num: float) -> bool:                                # Для проверки варианта вывода
    return num % 1 == 0



number = abs(float(input("Введите число: ")))
print("Введите в какую систему вы хотите перевести число:  ")
binary_num: int = int(input(f"Двоичная =>  <<2>> ----- Восьмиричная => <<8>>  "))
binary_num = numb_check(binary_num, 2, 8)
print("Введите метод выполнения перевода в систему исчисления.")
method_exec: int = int(input(
    "Для использования метода рекурсии нажмите: <<1>>.\nДля использования метода циклом нажмите:   <<2>>  "))
method_exec = numb_check(method_exec, 1, 2)

number = Decimal(str(number))
num_int = int(number)
float_part = number - num_int
num_length = len(str(number))
getcontext().prec = num_length
                          # У меня версия Python 3.8. Нельзя через match >>> case >>> default реализовать.

if binary_num == 2 and method_exec == 1:        # РЕКУРСИЯ ДЛЯ ДВОИЧИНОЙ СИС. ИСЧ.
    num_2: int = num_int
    list_rec_2: list = convert_num_rec(num_2, 2)
    list_float_rec_2: list  = convert_float_part_rec(float_part, 2, num_length)
    print(f"Число {number} в двоичной системе исчисления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_rec_2)))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_rec_2[::-1])))
    else:
        print("".join(map(str, list_rec_2)), end=".")
        print("".join(map(str, list_float_rec_2[::-1])))

elif binary_num == 2 and method_exec == 2:           # ЦИКЛ ДЛЯ ДВОИЧИНОЙ СИС. ИСЧ.
    num_2: int = num_int
    list_loop_2: list  = convert_num_loop(num_2, 2)
    list_float_2: list  = convert_float_part_loop(float_part, 2, num_length)
    print(f"Число {number} в двоичной системе исчисления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_loop_2[::-1])))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_2)))
    else:
        print("".join(map(str, list_loop_2[::-1])), end=".")
        print("".join(map(str, list_float_2)))

elif binary_num == 8 and method_exec == 1:             # РЕКУРСИЯ ДЛЯ ВОСЬМЕРИЧНОЙ СИС. ИСЧ.
    num_8: int = num_int
    list_rec_8: list  = convert_num_rec (num_8, 8)
    list_float_rec_8: list  = convert_float_part_rec(float_part, 8, num_length)
    print(f"Число {number} в восьмеричной системе исчисления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_rec_8)))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_rec_8[::-1])))
    else:
        print("".join(map(str, list_rec_8)), end=".")
        print("".join(map(str, list_float_rec_8[::-1])))

else:                                                    # ЦИКЛ ДЛЯ ВОСЬМЕРИЧНОЙ СИС. ИСЧ.
    num_8: int = num_int
    list_loop_8: list  = convert_num_loop (num_8, 8)
    list_float_rec_8: list  = convert_float_part_loop(float_part, 8, num_length)
    print(f"Число {number} в восьмеричной системе исчисления: ", end="=> ")
    if out_answer_check (number):
        print("".join(map(str, list_loop_8[::-1])))
    elif num_int == 0:
        print(f"{num_int}", end=".")
        print("".join(map(str, list_float_rec_8)))
    else:
        print("".join(map(str, list_loop_8[::-1])), end=".")
        print("".join(map(str, list_float_rec_8)))


