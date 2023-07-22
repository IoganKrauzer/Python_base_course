# дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
# например был список [1,15,55,7.58,0,99]
# и пользователь ввел 5
# ответ будет 4


# дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
# например был список [1,15,55,7.58,0,99]
# и пользователь ввел 5
# ответ будет 4

# n = [1, 15, 55, 7.58, 0, 99]
# count = 0
# i = 0
# while i < len(n):
#     if n[i]//10 or n[i] % 10 == 5 :
#         count +=1
#     i+=1
# print(count)


# доп задача для тех кто решил все задачи второй части семинара
# дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
# например был список [1,15,55,7.58,0,99]
# и пользователь ввел 5
# ответ будет 4
# from decimal import *


# def numbers_after_dot_converter(number):
#     numbers_after_dot = (Decimal (str(number)).as_tuple().exponent*(-1))
#     while numbers_after_dot > 0:
#         number *= 10
#         numbers_after_dot -= 1
#     return round(number)

# def calc(list):
#     count = 0
#     for i in range(len(list)):
#         while list[i] != 0:
#             if list[i] % 10 == 5:
#                 count += 1
#             list[i] = list[i] // 10
#     return count
                
                
# sp = [1,15,55,7.58,0,99]

# sp2 = []
# for i in range(len(sp)):
#     sp2.append(numbers_after_dot_converter(sp[i]))
    
# print(sp)
# print(sp2)
# a = calc(sp2)
# print(a)