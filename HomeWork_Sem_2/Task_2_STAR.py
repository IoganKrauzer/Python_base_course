#  задача Де моргана необязательная
#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  теперь надо проверить ее практически в цикле 100 раз прогоняем
#  каждый раз генерируем случайное количество предикат от 3 до 15
#  и конечно со случайным булевым значением
#  и засекаем общее время выполнения программы
#  юзаем библиотеки random и time
#  предикаты НЕ ЗАДАЕМ как целое число!

from random import choice
import os
os.system('cls')
import time


count = 0           # Если  левая часть эквивал правой, то счетчик увеличивается. Если по итогу счетчик != прогонам, то ошибка.
runs = int(input("Введите кол-во прогонов: "))
print("##################------S----T----A----R----T------###################") # обозначения начала интервала прогонов. Убедиться, что не глючит.
start = time.time()                                                             
for _ in range (runs):
    x = choice([True, False])       # на каждой итерации будет генерироваться случайное bool значение
    y = choice([True, False])
    z = choice([True, False])
    print(f"Сгенерированные [{x}, {y} ,{z}]")
    l_half = not(x or y or z)                    #bool выражение для левой стороны
    r_half = (not x) and (not y) and (not z)     #bool выражение для правой стороны
    flag = False                                # флаг обнуляется на каждой итерации 

    if l_half == r_half:
        flag = True
        count += 1                  
    else:
        flag
    print(f">>>---{flag}---<<<")
end = time.time()

print(round((end-start),7) , "ms")

print(count)    
if count == runs:
    print(f"Было проведено {runs} прогонов. Теорема верна. ")   
else:
    print("Error.")
print(f"Время выполнения {runs} прогонов составляет: {round((end-start),7)} ms")

print("#######################------E----N----D------######################")

# from random import *
# # x = choice([True,False])
# # y = choice([True,False])
# # z = choice([True,False])

# def predicate_generator(predicate_count):
#     predicates = []
#     for i in range(predicate_count):
#         predicates.append(choice([True,False]))
#     return predicates



# def de_morgan(predicates):
#     left_side = predicates[0]
#     right_side = not predicates[0]
#     for i in range(1,len(predicates)):
#         left_side = left_side or predicates[i]
#         right_side = right_side and not predicates[i]
#     return not left_side == right_side       
        

# j = 0
# while(j < 100):
#     count_predicate = randint(3,15)
#     print(de_morgan(predicate_generator(count_predicate)))
#     j += 1

# from random import choice, randint
# from time import time
# start = time()

# for _ in range(100):
#     sp = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
#     new_sp = list()
#     for i in range(randint(3, 15)):
#         sp[i] = choice([True, False])
#         new_sp.append(sp[i])
    
#     #print(new_sp)
#     left_side = False
#     right_side = True
    
#     for i in range(len(new_sp)):
#         tmp_left = new_sp[i]
#         left_side = left_side or tmp_left
#         tmp_right = new_sp[i]
#         right_side = right_side and not tmp_right

#     if not left_side == right_side:
#         print('Statement is true')
#     else:
#         print('Statement is false')

# end = time()-start
# print(end)