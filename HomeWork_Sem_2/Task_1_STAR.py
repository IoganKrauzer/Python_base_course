 #Посчитать сумму цифр любого целого или вещественного числа.
import os
os.system('cls')
from decimal import Decimal
# import  decimal


def num_to_int (n):    #обработка числа 
    if n % 1 != 0:
        while n % 1 != 0:
            n *= 10
        return n
    else:
        return n


def sum_of_num (n):    #сумма цифр в числе
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return int(sum)


def check_number_out(n):    # для вывода целого числа без 00. 46.00 => 46
    if n % 1 !=0:
        return n
    else: 
        return int(n)



num = float(input("Введите число "))
num = Decimal(str(num))
print (f"Сумма цифр в числe {check_number_out(num)} равняется: {sum_of_num(num_to_int (num))}")




