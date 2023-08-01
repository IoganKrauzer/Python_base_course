# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

def get_numbers_pair(user_list):
    count: int = 0
    for i in range(len(user_list) - 1):
        for j in range(i + 1, len(user_list)):
            if user_list[i] == user_list[j]:
                count += 1
    return count
            
data_list: list = [1, 2, 3, 2, 3]
print(get_numbers_pair(data_list))