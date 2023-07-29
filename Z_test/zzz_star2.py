# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
import random
import os
os.system('cls')


def create_polynomial(polyn_list):
    def generate_oper ():
        return random.choice(['+', '-'])
    _length = len(polyn_list)
    l_degree = []
    for i in range (_length - 1, - 1, -1):
        l_degree.append(i)
    # print("Степени многочленов:  ", l_degree)
    stroke = ""
    for i in range (_length):    
        if polyn_list[i] == 0 or l_degree[i] == 0:
            if polyn_list[i] != 0 or l_degree[i] == 0:
                stroke += f"{polyn_list[i]}"
            else:
                continue
            if i > 0 and i < _length - 1:
                stroke += f" {generate_oper ()} "
        elif polyn_list[i] == 1 or l_degree[i] == 1:
            if polyn_list[i] == 1 and l_degree[i] != 1:
                stroke += f"x^{l_degree[i]}"
            elif polyn_list[i] != 1 and l_degree[i] == 1:
                stroke += f"{polyn_list[i]}x"
            if i < _length - 1:
                stroke += f" {generate_oper ()} "
        elif i < _length -1:
            stroke += f"{polyn_list[i]}x^{l_degree[i]}"
            if i < _length - 1:
                stroke += f" {generate_oper ()} " 
        else:
            stroke += f"{polyn_list[i]}x"
    stroke += " = 0"
    return stroke


#[0,8,1,10]  - >  8*x^2 + x +10 = 0
# 0 1 2 3  => index
# 3 2 1 0  => defree

k = 4
polyn_list_1 = [random.randint(0, 10) for _ in range (random.randint(2, 6))]
polyn_list_2 = [random.randint(0, 10) for _ in range (random.randint(2, 6))]

print("Список сгенерированный 1 => ", polyn_list_1)
print("Список сгенерированный 2 => ", polyn_list_2)
print(create_polynomial(polyn_list_1))
print(create_polynomial(polyn_list_2))


#-----------T---E---M---P----------


# (i > 0 and i < _length - 1):

#[0,8,1,10]  - >  8*x^2 + x +10 = 0
# 0 1 2 3  => index
# 3 2 1 0  => defree







#----------------------B--I--N--------------------------------



# k = int(input("Введите натуральную максимальную степень "))
# sp = [randint(0,10) for _ in range(k+1)]
# print(sp)
# #[0,8,1,10]  - >  8*x^2 + x +10 = 0