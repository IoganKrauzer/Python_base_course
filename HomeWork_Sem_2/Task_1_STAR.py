 #Посчитать сумму цифр любого целого или вещественного числа.
import os
os.system('cls')
from decimal import Decimal, getcontext
import  decimal




# num = Decimal(str(num))
# count = 0

# num = Decimal(str(0.46))


# while num % 1.0 != 0:
#     num *= 10
#     count += 1
# print (num)
# temp = count / 2
# for i in range (8):
#     num //= 10
# print (count)
# print (num)
# num = Decimal(str(num))


# # num = Decimal(str(num))
# getcontext().prec = 5
# print(getcontext())

# while Decimal(str(num)) % 1!= 0:
#     num *= 10
#     print (num)

num = 0.46
num_dec = Decimal(str(num))
getcontext().prec = len(str(num))
while num_dec % 1 != 0:
    num_dec *= 10


print(num_dec)








