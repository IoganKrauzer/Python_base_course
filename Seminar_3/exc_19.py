# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


import os
os.system('cls')

l_1 = [1, 2, 3, 4, 5]
k = 4
print(l_1)
for i in range(k):
    l_1.extend(l_1[:k])
    del l_1[0:k]
    print(l_1)
# l_1.remove(l_1[:3])
# for i in range (3):
#     l_1.insert(0, l_1.pop()) 




# print (l_1)
# for i in range (k):
#     a = l_1.pop(len(l_1) - 1)
#     l_1.insert(0, a)

# print (l_1)

# print (l_1[k:] + l_1[:k])
