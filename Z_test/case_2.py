#  Задача 18: Требуется найти в массиве A[1..N] самый близкий по
#  величине элемент к заданному числу X. Пользователь в первой строке
#  вводит натуральное число N – количество элементов в массиве. В
#  последующих строках записаны N целых чисел Ai. Последняя строка
#  содержит число X
#  5
#  1 2 3 4 5
#  6
#  -> 5
import os
os.system('cls')


# list_1 = [1, 2, 3, 4, 5]
# k = 6
list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10
# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11


for i in range(len(list_1) - 1):
    min = i + 1
    for t  in range(i + 1,len(list_1)):
        if list_1[min] > list_1 [t]:
            min = t
    
    if list_1[i] > list_1[min]:
        temp = list_1[i]
        list_1[i] = list_1[min]
        list_1[min] = temp
        

print(list_1)
index = 0

if k >= list_1[0] and k <= list_1[len(list_1) - 1]:
    
    for i in range( len(list_1) - 1):
        if list_1[i] <= k and list_1[i + 1] >= k:        
            if k - list_1[i] > list_1[i + 1] - k:
                index = i+ 1
            else:
                index = i
    
    print(list_1[index])
elif k < list_1[0]:
    print(list_1[0])
else:
    print(list_1[len(list_1) - 1])


################## Best Answer###############

#[2, 4, 1, 6, 8, 2, 9, 3, 2, 5] // 10


m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)