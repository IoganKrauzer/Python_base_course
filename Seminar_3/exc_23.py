# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import os
os.system('cls')

list_1 = [0, -1, 5, 2, 3]
a_l = []
min = 0
for i in range(len(list_1)):
    if list_1[min] > list_1[i]:
        min = i

a_l.append(list_1[min])
print(a_l)

for i in range(len(list_1)):
    if list_1[i] > a_l[0]:
        a_l.append(list_1[i])
print(a_l)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


# v = [0, -1, 5, 2, 3]
# i = 1
# j = 0
# while i < len(v):
#     if v[i] > v[i-1]:

#         j+=1
#     i+=1
# print(j)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


# v = [0, -1, 5, 2, 3]
# i = 1
# j = 0
# while i < len(v):
#     if v[i] > v[i-1]:

#         j+=1
#     i+=1
# print(j)