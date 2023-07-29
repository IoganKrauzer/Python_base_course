# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


num = 16



def checkNum(num, i=2):
    if i == num:
        return True
    if num % i == 0:
        return False
    return checkNum(num, i + 1)


num = int(input("введите число "))

print(checkNum(num))