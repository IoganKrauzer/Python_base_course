# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import os
os.system('cls')




def rekursia (num, i = 0):
    if i == len(num):
        return num
    if num[i] == max(num):
        num[i] = min(num)
    rekursia(num, i + 1)




x = [1, 3, 4, 3, 4]
rekursia(x)
print(x)