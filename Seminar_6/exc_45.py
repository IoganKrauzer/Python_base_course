# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284




k = int(input("Введите число k: "))

def deliteli(value):    
    deliteli = []
    for num in range(1, value // 2 + 1):        
        if value % num == 0:
            deliteli.append(num)    
    return deliteli


for m in range(2, k):
    n = sum(deliteli(m))    
    if m == sum(deliteli(n)) and m < n:
        print(m, n)





# def all_divisors(n):
#     ans_list = [x  for x in range (1, n+1) if n % x == 0 and x != n]
    
    
        
#     return ans_list


# num = int(input("Введите число для нахождения делителей: "))
# # print("Список делителей: ", ", ".join(map(str, all_divisors(num))))
# summa = sum(all_divisors(num))
# print(summa)
# list_1 
# for m in range(num):
#     n = sum(all_divisors(m))
#     if m == sum(all_divisors(n)):




