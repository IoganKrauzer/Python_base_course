#  Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
#  ценность. В случае с английским алфавитом очки распределяются так:
#  ● A, E, I, O, U, L, N, S, T, R – 1 очко;
#  ● D, G – 2 очка;
#  ● B, C, M, P – 3 очка;
#  ● F, H, V, W, Y – 4 очка;
#  ● K – 5 очков;
#  ● J, X – 8 очков;
#  ● Q, Z – 10 очков.
#  А русские буквы оцениваются так:
#  ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#  ● Д, К, Л, М, П, У – 2 очка;
#  ● Б, Г, Ё, Ь, Я – 3 очка;
#  ● Й, Ы – 4 очка;
#  ● Ж, З, Х, Ц, Ч – 5 очков;
#  ● Ш, Э, Ю – 8 очков;
#  ● Ф, Щ, Ъ – 10 очков.
#  Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#  Будем считать, что на вход подается только одно слово, которое содержит либо только
#  английские, либо только русские буквы.
#  Ввод:
#  ноутбук
#  Вывод: 12
import os
os.system('cls')

k = 'apple'
# k_up = k.upper()
# count = 0

# for i in k_up:
#     if i in ("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"):
#         count += 1
#         continue
#     elif i in ("Д", "К", "Л", "М", "П", "У"):
#         count += 2
#         continue
#     elif i in ("Б", "Г", "Ё", "Ь", "Я"):
#         count += 3     
#         continue
#     elif i in  ("Й", "Ы"):
#         count += 4   
#         continue
#     elif i in ("Ж", "З", "Х", "Ц", "Ч"):
#         count += 5       
#         continue
#     elif i in ("Ш", "Э", "Ю"):
#         count += 8     
#         continue
#     elif i in ("Ф", "Щ", "Ъ"):
#         count += 10
#         continue
    
# for i in k_up:
#     if i in ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R"):
#         count += 1
#         continue
#     elif i in ("D", "G"):
#         count += 2
#         continue
#     elif i in ("B", "C", "M", "P"):
#         count += 3
#         continue
#     elif i in  ("F", "H", "V", "W", "Y"):
#         count += 4
#         continue
#     elif i in ("K"):
#         count += 5
#         continue
#     elif i in ("J", "X"):
#         count += 8
#         continue
#     elif i in ("Q", "Z"):
#         count += 10
#         continue
   
# print(count)



points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)



# scrabble_dictionaty = { 
#     1:'AEIOULNSTRАВЕИНОРСТ', 
#     2:'DGДКЛМПУ', 
#     3:'BCMPБГЁЬЯ', 
#     4:'FHVWYЙЫ', 
#     5:'KЖЗХЦЧ', 
#     8:'JXШЭЮ', 
#     10:'QZФЩЪ' 
#     } 
# word = input().upper() 
 
# print(sum([k for i in word for k, v in scrabble_dictionaty.items() if i in v]))