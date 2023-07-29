# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os
os.system('cls')
def rec (an, bn):
    if bn == 1:
        return an
    return  an* rec(an , bn -1)



    
a = 3
b = 5
print(rec (a, b))

