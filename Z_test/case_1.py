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
l_list = list()
for i in range (num):
    # l_list.append(int(input()))
    l_list.append(random.randint(1, 9))
print(l_list)

a = int(input())
count = 0
for i in l_list:
    if a == i:
        count += 1
print(count)
