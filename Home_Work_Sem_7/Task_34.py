# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

import os
os.system('cls')




def create_list(_stroke):
    _stroke = _stroke.split()
    return _stroke


def count_glass (_stroke):
    _glass_c_l = []
    for i in _stroke:
        count = 0
        for k in range(len(i)):
            if i[k] in ['а', 'у', 'е', 'о', 'я', 'и', 'ю']:
                count += 1
        _glass_c_l.append(count)
    return _glass_c_l
        

def check_glass_l(_glass_c_l):
    check_elem = _glass_c_l[0]
    flag = True
    for i in _glass_c_l:
        if check_elem != i:
            flag = False
    print("Парам пам-пам") if flag == True else print("Пам парам")




stroke = "пара-ра-рам рам-пам-папам па-ра-па-да"
print(stroke)
stroke = create_list(stroke)
print(stroke)
glass_c_l = count_glass(stroke)
print(glass_c_l)
check_glass_l(glass_c_l)

