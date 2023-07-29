# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import os
os.system('cls')

l_1 = [1, 1, 2, 0, -1, 3, 4, 4]
l_2 = list()

for _ in l_1:
    if _ not in l_2:
        l_2.append(_)
print(l_2)
print(len(l_2))







# count = 0
# l_1 = set(l_1)
# print (l_1)
# for i in l_1:
#     count += 1
# print (count)

# data = [1, 1, 2, 0, -1, 3, 4, 4]
# print(data)
# different_numbers = []
# for number in data:
#     if number not in different_numbers:
#         different_numbers.append(number)
# print(f"Различных чисел: {len(different_numbers)}")