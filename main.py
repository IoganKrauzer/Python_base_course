# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
import random
import os
os.system('cls')


_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# indx_list_1 = [3, 2, 1, 0]                # ПОКА НЕ ИСПОЛЬЗУЕМ
# indx_list_2 = [4, 3, 2, 1, 0]

# polyn_list_1 = [1, 5, 6, 4]
# polyn_list_2 = [4, 3, 0, 6, 7]

# polyn_str_1 = "x^3 - 5x^2 - 6x - 4 = 0"     # С ПРОБЕЛАМИ
# polyn_str_2 = "4x^4 - 3x^3 + 6x + 7 = 0"

# polyn_str_1 = "x^3-5x^2-6x-4=0"
# polyn_str_2 = "4x^4-3x^3+6x+7=0"

# polyn_str_1 = []
# count_helper = 0
# for i in polyn_str_1:
#     polyn_str_1.append(i)

# list_for_polyn2 = []
# count_helper = 0
# for i in polyn_str_2:
#     list_for_polyn2.append(i)



def create_indx_lists(polyn_str_l):                # ИНДЕКСЫ ЛИСТ
    _polyn_indx = []
    for i in range (len(polyn_str_l) - 1):
        if polyn_str_l[i] == "^":
            _polyn_indx.append(polyn_str_l[i+1])
        elif polyn_str_l[i - 1] == "x":
            _polyn_indx.append('1')
        elif polyn_str_l[i + 1] == "=" :
            _polyn_indx.append('0')

    if _polyn_indx[0] != len(_polyn_indx) - 1:             
        _polyn_indx_checked = []
        k = 0
        up_degree = int(_polyn_indx[0])
        while k <= up_degree:
            _polyn_indx_checked.insert(0, k)
            k += 1
        return _polyn_indx_checked
    return _polyn_indx
    


# def create_coef_list (polyn_str_l, indx_list):
#     list_for_coef = []
#     for i in range (len(polyn_str_l) - 1):
#         if polyn_str_l[i + 1] == "x" or polyn_str_l[i + 1] == "=" or polyn_str_l[i] == "+" or polyn_str_l[i] == "-":
#             list_for_coef.append(polyn_str_l[i])
#         elif polyn_str_l[i] == "x" and i == 0:
#             list_for_coef.append('1')
#     return list_for_coef

# def create_coef_list (polyn_str_l, indx_list):
#     list_for_coef = []
#     _check_count = 0
    
#     for i in range (len(polyn_str_l) - 1):
#         if polyn_str_l[i + 1] == "x" or polyn_str_l[i + 1] == "=" :
#             list_for_coef.append(polyn_str_l[i])
#         elif polyn_str_l[i] == "x" and i == 0 or polyn_str_l[i] == "x" and polyn_str_l[i+1] != "^" :
#             list_for_coef.append('1')
#         elif 
#         count += 1
#     return list_for_coef
# -----------------------------------------------------------------------------------------------------

def create_coef_list (polyn_str_l, indx_list):
    list_for_coef = []
    _check_count = 0
    _check_char = ['+', '-']
    for i in indx_list:
        num_check = f"^{i}"
        if i == 0:
            for k in range (len(polyn_str_l) - 1):
                if polyn_str_l[k + 1] == "=" and polyn_str_l[k -1] != "^" or polyn_str_l[k + 1] == "=" and polyn_str_l[k] != "x":
                    list_for_coef.insert(_check_count, polyn_str_l[k])
                    break
                elif polyn_str_l[k + 1] == "=" and polyn_str_l[k] == "x":
                    list_for_coef.insert(_check_count, '0')
                    break
                
        elif i == 1:
            for j in range (len(polyn_str_l) - 1):
                if polyn_str_l[j + 1] in _check_char and polyn_str_l[j] == "x":
                    if polyn_str_l[j - 1] in _check_char:
                        list_for_coef.append("1")
                    else:
                        list_for_coef.append(polyn_str_l[j - 1])
                    break

        elif num_check in polyn_str_l:
            for p in range (len(polyn_str_l) - 1):
                if polyn_str_l[p + 1] == '^' and polyn_str_l[p + 2] == f'{i}':
                    if p == 0 or p != 0 and polyn_str_l[p - 1] in _check_char: 
                        list_for_coef.append("1")
                        break
                    else:
                        list_for_coef.append(polyn_str_l[p - 1])
                        break

        elif num_check not in polyn_str_l:
            list_for_coef.append("0")
        
        _check_count += 1

    return list_for_coef


                         

                                                                            # 4x^4



                  



#                                                         4x^4-3x^3+6x+7=0
#                                                         6x^2=0
#                                                         6x=0



# -----------------------------------------------------------------------------------------------------
# def create_coef_list (polyn_str_l, indx_list):
   
#     def help_with_check_count(count, indx_list):
#         if count < len(indx_list) - 1:
#             count += 1
#             return count
#         return count

#     list_for_coef = []
#     _check_count = 0
#     for i in range (0, len(polyn_str_l) - 1):
#         _help_char = f"^{indx_list[_check_count]}"
#         if polyn_str_l[i + 1] == "x" or polyn_str_l[i + 1] == "=" :
#             list_for_coef.append(polyn_str_l[i]) 
#             _check_count = help_with_check_count(_check_count, indx_list)
#             continue
        
#         elif polyn_str_l[i] == "x" and i == 0 or polyn_str_l[i] == "x" and polyn_str_l[i+1] != "^":
#             list_for_coef.append('1')
#             _check_count = help_with_check_count(_check_count, indx_list)
#             continue
#             # print(list_for_coef[_check_count])
#         elif _help_char not in polyn_str_l and indx_list[_check_count] > 1:
#             list_for_coef.append('0')
#             _check_count = help_with_check_count(_check_count, indx_list)
#             continue
#     return list_for_coef
# -----------------------------------------------------------------------------------------------------
#                "x^3-5x^2-6x-4=0"  --- МНОГОЧЛЕН 1
#                "4x^4-3x^3+6x+7=0" --- МНОГОЧЛЕН 2      4x^4-3x^3+6x+7=0
#                                                         6x^2=0
#                                                         6x=0

#                [3, 2, 1, 0]       --- ИНДЕКСЫ 1        [4, 3, 2, 1, 0]
#                [4, 3, 2, 1, 0]    --- ИНДЕКСЫ 2        [4, 3, 0, 6, 7]
# polyn_list_1 = [1, 5, 6, 4]       --- КОЭФ 1
# polyn_list_2 = [4, 3, 0, 6, 7]    --- КОЭФ 1

polyn_str_1 = "x^3-5x^2-6x-4=0"
polyn_str_2 = "4x^4-3x^3+6x+7=0"
# indx_l_1 = create_indx_lists(polyn_str_1)
indx_l_1 = [3, 2, 1, 0]
# indx_l_2 = create_indx_lists(polyn_str_2)
indx_l_2 = [4, 3, 2, 1, 0]
# print(indx_l_1)
# print(indx_l_2)
polyn_coef_list_1 = create_coef_list (polyn_str_1, indx_l_1)
polyn_coef_list_2 = create_coef_list (polyn_str_2, indx_l_2)
print(polyn_coef_list_1)
print(polyn_coef_list_2)













# --------------------------

# print(polyn_str_1)
# print(list_for_polyn2)
# print(list_for_coef)
# print(list_for_coef_2)
# --------------------------
# def create_indx_lists(polyn_str_l):
#     _polyn_indx = []
#     for i in range (len(polyn_str_l) - 1):
#         if polyn_str_l[i] == "^":
#             _polyn_indx.append(polyn_str_l[i+1])
#         elif polyn_str_l[i - 1] == "x":
#             _polyn_indx.append('1')
#         elif polyn_str_l[i + 1] == "=" :
#             _polyn_indx.append('0')

#     if _polyn_indx[0] != len(_polyn_indx) - 1:             
#         _polyn_indx_checked = []
#         k = 0
#         up_degree = int(_polyn_indx[0])
#         while k <= up_degree:
#             _polyn_indx_checked.insert(0, k)
#             k += 1
#         return _polyn_indx_checked
#     return _polyn_indx

# indx_l_1 = create_indx_lists(polyn_str_1)
# indx_l_2 = create_indx_lists(polyn_str_2)
# print(indx_l_1)
# print(indx_l_2)






# polyn_str_1 = "x^3-5x^2-6x-4=0"
# polyn_str_2 = "4x^4-3x^3+6x+7=0"



#                           --------------------------------------
#                              [1, 5, 6, 4]    "x^3-5x^2-6x-4=0"
#                              [4, 3, 0, 6, 7] "4x^4-3x^3+6x+7=0"
#                           --------------------------------------



# for i in range (len(polyn_str_1) -1, -1, -1):
#     if polyn_str_1[i] == "0" or polyn_str_1[i] == "=" or polyn_str_1[i] == "+" or polyn_str_1[i] == "-":
#         polyn_str_1.insert(count_helper, polyn_str_1[i])
#     count_helper += 1
    



# for i in range (len(polyn_str_1) - 1, -1, -1):
#     print(polyn_str_1[i])










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