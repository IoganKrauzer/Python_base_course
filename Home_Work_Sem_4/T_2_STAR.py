# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
import random
import os
os.system('cls')




# def create_polynomial(polyn_list):
#     def generate_oper ():
#         return random.choice(['+', '-'])
#     _length = len(polyn_list)
#     l_degree = []
#     for i in range (_length - 1, - 1, -1):
#         l_degree.append(i)
#     print("Список индексов ", l_degree)
#     stroke = ""
#     for i in range (_length):    
#         if polyn_list[i] == 0 or l_degree[i] == 0:
#             if polyn_list[i] != 0 or l_degree[i] == 0:
#                 stroke += f"{polyn_list[i]}"
#             else:
#                 continue
#             if i > 0 and i < _length - 1:
#                 stroke += f" {generate_oper ()} "
#         elif polyn_list[i] == 1 or l_degree[i] == 1:
#             if polyn_list[i] == 1 and l_degree[i] != 1:
#                 stroke += f"x^{l_degree[i]}"
#             elif polyn_list[i] != 1 and l_degree[i] == 1:
#                 stroke += f"{polyn_list[i]}x"
#             else:
#                 stroke += "x"
#             if i < _length - 1:
#                 stroke += f" {generate_oper ()} "
#         elif i < _length -1:
#             stroke += f"{polyn_list[i]}x^{l_degree[i]}"
#             if i < _length - 1:
#                 stroke += f" {generate_oper ()} " 
#         else:
#             stroke += f"{polyn_list[i]}x"
#     stroke += " = 0"
#     return stroke




# k = 4
# polyn_list_1 = [random.randint(0, 10) for _ in range (random.randint(2, 6))]
# polyn_list_2 = [random.randint(0, 10) for _ in range (random.randint(2, 6))]

# print("Список сгенерированный 1 => ", polyn_list_1)
# print("Список сгенерированный 2 => ", polyn_list_2)
# print(create_polynomial(polyn_list_1))
# print(create_polynomial(polyn_list_2))

# polyn_str_1 = create_polynomial(polyn_list_1)
# polyn_str_2 = create_polynomial(polyn_list_2)
# print(polyn_str_1)
# print(polyn_str_2)








indx_list_1 = [3, 2, 1, 0]
indx_list_2 = [4, 3, 2, 1, 0]

polyn_list_1 = [1, 5, 6, 4]
polyn_list_2 = [4, 3, 0, 6, 7]

polyn_str_1 = "x^3 - 5x^2 - 6x - 4 = 0"
polyn_str_2 = "4x^4 - 3x^3 + 6x + 7 = 0"





# def index_list (l_list):
#     l_degree = []
#     for i in range (len(l_list) - 1, - 1, -1):
#         l_degree.append(i)
#     return l_degree
    



# polyn_list_1 = [8, 10, 4, 0, 9, 9]
# polyn_list_2 = [0, 0, 4, 4, 5, 1]

# polyn_str_1 = "8x^5 - 10x^4 - 4x^3 - 9x - 9 = 0"
# polyn_str_2 = "4x^3 + 4x^2 - 5x + 1 = 0"
# print(polyn_str_1)
# print(polyn_str_2)
# indx_list_1 = index_list (polyn_list_1)
# indx_list_2 = index_list (polyn_list_2)
# print(indx_list_1)
# print(indx_list_2)




#[0,8,1,10]  - >  8*x^2 + x +10 = 0
# 0 1 2 3  => index
# 3 2 1 0  => defree