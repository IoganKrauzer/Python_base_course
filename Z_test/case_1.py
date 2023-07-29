#  Задача 16: Требуется вычислить, сколько раз встречается некоторое
#  число X в массиве A[1..N]. Пользователь в первой строке вводит
#  натуральное число N – количество элементов в массиве. В последующих
#  строках записаны N целых чисел Ai. Последняя строка содержит число X
#  5
#  1 2 3 4 5
#  3
#  -> 1
import random
import os
os.system('cls')




num = 5
# x = int(input())
x = 5
l_list = [] * num
for i in range (1, num + 1):
    l_list.append(i)
print(l_list)
count = 0
for k in l_list:
    if k == x:
        count += 1
print(count)
# a = int(input())
# count = 0
# for i in l_list:
#     if a == i:
#         count += 1
# print(count)



# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)