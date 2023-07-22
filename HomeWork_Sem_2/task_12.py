# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# 5 , 7
# 5 + 7 = 12
# 5* 7 = 35


import os
os.system('cls')


def numb_check(num):
    while num > 1000:
        num = abs(
            int(input("Число превышает указанный диапозон. Загадайте другое число ")))
    return num


a = abs(int(input("Загадайте первое число ")))
b = abs(int(input("Загадайте второе число ")))
a = numb_check(a)
b = numb_check(b)

sum_of_numbers = a + b
mult_of_num = a * b

print(f"Первая подсказка! Сумма двух чисел: {sum_of_numbers}")
print(f"Вторая подсказка! Произведение двух чисел: {mult_of_num}")

list_1 = list()
list_1 = [(x, sum_of_numbers - x) for x in range(1, sum_of_numbers + 1)
          if x * (sum_of_numbers - x) == mult_of_num]

print(f"Первое загаданное число: {list_1[0][0]}")
print(f"Второе загаданное число: {list_1[0][1]}")
