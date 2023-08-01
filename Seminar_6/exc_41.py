# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
import random




# def get_quantity_el(list_1: list) -> int:
#     count: int = 0
#     for i in range(len(list_1)):
#         if i == 0:
#             if list_1[i] > list_1[i + 1] and list_1[i] > list_1[-1]:
#                 count += 1
#         elif i < len(list_1) - 1:        
#             if list_1[i] > list_1[i + 1] and list_1[i] > list_1[i - 1]:
#                 count += 1
#         elif i == len(list_1) - 1:
#             if list_1[i] > list_1[0] and list_1[i] > list_1[i - 1]:
#                 count += 1
#     return count
# data_list: list = [5, 4, 3, 2, 1, 5, 3]
# print(get_quantity_el(data_list))



def check_neighbours(index, array):    
    if array[(index + 1) % len(array)] < array[index] and array[index - 1] < array[index]:
        return True


arr_length = int(input("Введите N: "))
arr = [random.randint(1, 5) for _ in range(arr_length)]
print(arr)
result = [1 for index in range(len(arr)) if check_neighbours(index, arr)]
print(sum(result))



# sp1 = [1,2,3,4,5]
# sp2 = [1,5,1,5,1]

# def both_less(sp):
#     count = 0
#     for i in range(len(sp)):
#         if sp[i - 1] < sp[i] and sp[i] > sp[i - len(sp) + 1]:
#             count += 1
#     print(count)
# both_less(sp1)
# both_less(sp2)


# sp = [randint(0, 5) for _ in range(10)]
# summ = 0
# for i in set(sp):
#     # print(i, sp.count(i))
#     summ += sp.count(i) // 2

# print(sp)
# print(summ)


# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

#1 2 3 2 3  вывод 2

# sp = [randint(0, 5) for _ in range(10)]
# summ = 0
# for i in set(sp):
#     # print(i, sp.count(i))
#     summ += sp.count(i) // 2

# print(sp)
# print(summ)