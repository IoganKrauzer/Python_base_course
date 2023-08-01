# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
import random
import os
os.system('cls')




def create_polynomial(polyn_list):                  # ГЕНЕРАЦИЯ МНОГОЧЛЕНА
    def generate_oper ():                           # ГЕНЕРАЦИЯ СЛУЧАЙНОГО ЗНАКА
        return random.choice(['+', '-'])
    _length = len(polyn_list)
    l_degree = []
    for i in range (_length - 1, - 1, -1):          # СПИСОК ДЛЯ ВЫСТАВЛЕНИЯ СТЕПЕНЕЙ
        l_degree.append(i)
    print("Список индексов ", l_degree)
    stroke = ""
    for i in range (_length):    
        if polyn_list[i] == 0 or l_degree[i] == 0:
            if polyn_list[i] != 0 or l_degree[i] == 0:
                stroke += f"{polyn_list[i]}"
            else:
                continue
            if i > 0 and i < _length - 1:
                stroke += f"{generate_oper()}"
        elif polyn_list[i] == 1 or l_degree[i] == 1:
            if polyn_list[i] == 1 and l_degree[i] != 1:
                stroke += f"x^{l_degree[i]}"
            elif polyn_list[i] != 1 and l_degree[i] == 1:
                stroke += f"{polyn_list[i]}x"
            else:
                stroke += "x"
            if i < _length - 1:
                stroke += f"{generate_oper()}"
        elif i < _length -1:
            stroke += f"{polyn_list[i]}x^{l_degree[i]}"
            if i < _length - 1:
                stroke += f"{generate_oper()}" 
        else:
            stroke += f"{polyn_list[i]}x"
    stroke += "=0"
    return stroke


def create_indx_lists(polyn_str_l):               # Так как у нас для сложения даны только многочлены
    _polyn_indx = []                              # То начнем с составления списка индексов
    for i in range (len(polyn_str_l) - 1):
        if polyn_str_l[i] == "^":
            _polyn_indx.append(polyn_str_l[i+1])
        elif polyn_str_l[i] == "x" and polyn_str_l[i+1] !='^':
            _polyn_indx.append('1')
        elif polyn_str_l[i + 1] == "=" and polyn_str_l[i] != "x":
            _polyn_indx.append('0')

    if _polyn_indx[0] != len(_polyn_indx) - 1:    # Тут идет замена типа данных со стр на инт       
        _polyn_indx_checked = []                  # Можно было сделать это в блоке выше.
        k = 0                                     
        up_degree = int(_polyn_indx[0])           
        while k <= up_degree:
            _polyn_indx_checked.insert(0, k)
            k += 1
        return _polyn_indx_checked
    return _polyn_indx
    

def create_coef_list (polyn_str_l, indx_list):    # Создаем списки коэффициентов и преобразуем их в тип INT
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
    for p in range (len(list_for_coef)):
        list_for_coef[p] = int (list_for_coef[p])
    return list_for_coef


def indx_list_check(indx_l, list_for_coef):             # Выравниваем и дозаполняем список индексов
    i = 0
    if len(indx_l) < len(list_for_coef):
        while len(indx_l) !=  len(list_for_coef) :
            indx_l.insert(i, len(list_for_coef) - 1 - i)
            i += 1
    return indx_l


def coeff_lists_check(polyn_coef_l_1, polyn_coef_l_2):   # Дозаполняем список коэффициентов
    i = 0                                                #
    if len(polyn_coef_l_1) > len(polyn_coef_l_2):
        while len(polyn_coef_l_1) != len(polyn_coef_l_2):
            polyn_coef_l_2.insert(i, 0)
            i += 1
        return polyn_coef_l_2
    elif len(polyn_coef_l_1) < len(polyn_coef_l_2):
        while len(polyn_coef_l_1) != len(polyn_coef_l_2):
            polyn_coef_l_1.insert(i, 0)
            i += 1
        return polyn_coef_l_1
   

def char_list(_polyn_str):                              # Создаем список знаков для каждого многочлена
    _count_help = 0                                     # Понадобится для функции create_lis_for_sum()
    _char_list = []
    for i in range (len(_polyn_str) -1, -1, -1):
        if _polyn_str[i] == '+' or _polyn_str[i] == '-':
            _char_list.insert( 0, _polyn_str[i])
            _count_help += 1      
    return _char_list


def create_lis_for_sum(_polyn_coef_l, _char_list):     # Создаем список с коэфф и знаками
    def _count_check(_h_count, _char_l):
        if _h_count < len(_char_l) - 1:
            _h_count += 1
            return _h_count
        return _h_count

    _list_for_sum = []
    _help_count = 0

    for i in range (len(_polyn_coef_l)):
        if _polyn_coef_l[i] == 0 and i == 0:
            _list_for_sum.append(_polyn_coef_l[i]) 
            continue
        elif _polyn_coef_l[i] == 0 :
            _list_for_sum.append('-') 
            _list_for_sum.append(_polyn_coef_l[i]) 
            continue
        elif _polyn_coef_l[i] != 0 and i == 0:
            _list_for_sum.append(_polyn_coef_l[i]) 
            continue
        elif _polyn_coef_l[i] != 0 and _polyn_coef_l[i - 1] != 0:
            _list_for_sum.append(_char_list[_help_count]) 
            _list_for_sum.append(_polyn_coef_l[i]) 
            _help_count = _count_check(_help_count, _char_list)
        elif _polyn_coef_l[i] != 0 and _polyn_coef_l[i - 1] == 0:
            _list_for_sum.append(_char_list[_help_count]) 
            _list_for_sum.append(_polyn_coef_l[i]) 
            _help_count = _count_check(_help_count, _char_list)
    return _list_for_sum


def math_oper_with_polyn(_list_f_sum_1, _list_f_sum_2):     # Создаем список с результатом математ операций
    _list_create_sum_answer = []                            # двух многочленов
    for i in range (0, len(_list_f_sum_1), 2):
        if i == 0:
            _list_create_sum_answer.append(_list_f_sum_1[i] + _list_f_sum_2[i])
        elif _list_f_sum_1[i - 1] == '-' and _list_f_sum_2[i - 1] == '-':
            _list_create_sum_answer.append(-_list_f_sum_1[i] + (-_list_f_sum_2[i]))
        elif _list_f_sum_1[i - 1] == '+' and _list_f_sum_2[i - 1] == '-':
            _list_create_sum_answer.append(_list_f_sum_1[i] + (-_list_f_sum_2[i]))
        elif _list_f_sum_1[i - 1] == '-' and _list_f_sum_2[i - 1] == '+':
            _list_create_sum_answer.append(-_list_f_sum_1[i] + _list_f_sum_2[i])
        elif _list_f_sum_1[i - 1] == '+' and _list_f_sum_2[i - 1] == '+':
            _list_create_sum_answer.append(_list_f_sum_1[i] + _list_f_sum_2[i])
    return _list_create_sum_answer    


def sum_of_two_polyn (_list_create_sum_answer):             # На основании списка создаем многочлен
    def check_sign(num):                                    # Проверяем знак
        _sign = ''
        if num > 0:
            _sign = '+'
            return _sign
        elif num < 0:
            return _sign

    _idex_list = []                                         # Список степеней
    for t in range(len(_list_create_sum_answer)):
        _idex_list.append(len(_list_create_sum_answer) - 1 - t)
  
    _stroke_answ = ""
    for i in range(len(_list_create_sum_answer)):           # Создаем строку многочлена
        if _list_create_sum_answer[i] == 0:
            continue
        elif abs(_list_create_sum_answer[i]) == 1: 
            if _idex_list[i] == 0 and i == 0:
                _stroke_answ += f"1"
            elif _idex_list[i] == 1 and i == 0:   
                _stroke_answ += f"x"  
            elif _idex_list[i] > 1 and i == 0:                
                _stroke_answ += f"x^{_idex_list[i]}"
            elif _idex_list[i] == 0 and i != 0:
                _stroke_answ += f"{check_sign(_list_create_sum_answer[i])}1"
            elif _idex_list[i] == 1 and i != 0:
                 _stroke_answ += f"{check_sign(_list_create_sum_answer[i])}x"
            elif _idex_list[i] > 1 and i != 0:
                 _stroke_answ += f"{check_sign(_list_create_sum_answer[i])}x^{_idex_list[i]}"
        elif abs(_list_create_sum_answer[i]) > 1:
            if _idex_list[i] == 0 and i == 0:
                _stroke_answ += f"{_list_create_sum_answer[i]}"
            elif _idex_list[i] == 1 and i == 0:   
                _stroke_answ += f"{_list_create_sum_answer[i]}x"  
            elif _idex_list[i] > 1 and i == 0:                
                _stroke_answ += f"{_list_create_sum_answer[i]}x^{_idex_list[i]}"
            elif _idex_list[i] == 0 and i != 0:
                _stroke_answ += f"{check_sign(_list_create_sum_answer[i])}{_list_create_sum_answer[i]}"
            elif _idex_list[i] == 1 and i != 0:
                 _stroke_answ += f"{check_sign(_list_create_sum_answer[i])}{_list_create_sum_answer[i]}x"
            elif _idex_list[i] > 1 and i != 0:
                 _stroke_answ += f"{check_sign(_list_create_sum_answer[i])}{_list_create_sum_answer[i]}x^{_idex_list[i]}" 
    _stroke_answ += "=0"
    return _stroke_answ




k = 4
polyn_list_1 = [random.randint(0, 10) for _ in range (random.randint(2, 6))]   
polyn_list_2 = [random.randint(0, 10) for _ in range (random.randint(2, 6))]
print("-------Г--Е--Н--Е--Р--А--Ц--И--Я-------М--Н--О--Г--О--Ч--Л--Е--Н--О--В")
print("Список сгенерированный 1 => ", polyn_list_1)
print("Список сгенерированный 2 => ", polyn_list_2)
polyn_stroke_1 = create_polynomial(polyn_list_1)
polyn_stroke_2 = create_polynomial(polyn_list_2)
print(polyn_stroke_1)
print(polyn_stroke_2)
print("------------------------------E---N---D-------------------------------")
print("\n-------------------------------S--T--A--R--T--------------------------")
polyn_str_1 = polyn_stroke_1
polyn_str_2 = polyn_stroke_2
# polyn_str_1 = "x^3-5x^2-6x-4=0"
# polyn_str_2 = "4x^4-3x^3+6x+7=0"
print("Первый многочлен: ", polyn_str_1)
print("Второй многочлен: ", polyn_str_2)
indx_l_1 = create_indx_lists(polyn_str_1)
indx_l_2 = create_indx_lists(polyn_str_2)
print("Индексы_1 : ", indx_l_1)
print("Индексы_2 : ", indx_l_2)
polyn_coef_list_1 = create_coef_list (polyn_str_1, indx_l_1)
polyn_coef_list_2 = create_coef_list (polyn_str_2, indx_l_2)
print("Лист кэффициентов_1: ", polyn_coef_list_1)
print("Лист кэффициентов_2: ", polyn_coef_list_2)
if len(polyn_coef_list_1) > len(polyn_coef_list_2):
    polyn_coef_list_2 = coeff_lists_check(polyn_coef_list_1, polyn_coef_list_2)
elif len(polyn_coef_list_1) < len(polyn_coef_list_2):
    polyn_coef_list_1 = coeff_lists_check(polyn_coef_list_1, polyn_coef_list_2)
print("Выравненный коэф_1: ", polyn_coef_list_1)
print("Выравненный коэф_2: ", polyn_coef_list_2)
indx_l_1 = indx_list_check(indx_l_1, polyn_coef_list_1)
indx_l_2 = indx_list_check(indx_l_2, polyn_coef_list_2)
print("Выравненные индексы_1", indx_l_1)
print("Выравненные индексы_2", indx_l_2)
char_list_1 = char_list(polyn_str_1)
char_list_2 = char_list(polyn_str_2)
print("Список знаков_1", char_list_1)
print("Список знаков_2", char_list_2)
list_for_sum_1 = create_lis_for_sum(polyn_coef_list_1, char_list_1)
list_for_sum_2 = create_lis_for_sum(polyn_coef_list_2, char_list_2)
print("Финальный список для вычислений_1", list_for_sum_1)
print("Финальный список для вычислений_2", list_for_sum_2)
list_create_sum_answer = math_oper_with_polyn(list_for_sum_1, list_for_sum_2)
print("Список со знаками и числами для создания ответа: ", list_create_sum_answer)
fin_answer = sum_of_two_polyn (list_create_sum_answer)
print("Ответ: => ", fin_answer)
print("----------------------F--I--N--I--S--H----------------------")
print("# Данный код написан кровью и потом в течение десятков часов\n# Спасибо за внимание! :)")


