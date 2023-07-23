 #Посчитать сумму цифр любого целого или вещественного числа.
import os
os.system('cls')
from decimal import Decimal, getcontext
import  decimal

def num_to_int (n):
    while n % 0 != 0:
        n *= 10


num = 0.46
num = Decimal(str(num))
print (num)




