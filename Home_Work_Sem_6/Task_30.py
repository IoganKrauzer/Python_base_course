# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
import os
os.system('cls')




def math_oper(n, d, a):
    _list_answer = [(lambda n, d, a: a + (n - 1) * d) ( n, d, a) for n in range(1, n + 1)]
    return _list_answer


_n = int(input("Введите длинну последовательности: "))
_d = int(input("Введите разницу: "))
_a = int(input("Введите первый элемент: "))
print(math_oper(_n, _d, _a))