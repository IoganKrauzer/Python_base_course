# Задача №31. Общее обсуждение
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21



def find_fibo(n):
    if (n == 0): 
        return 0 
    if (n == 1): 
        return 1
    return find_fibo((n - 2)) + find_fibo((n - 1))

num = int(input("Введите число: "))
print(find_fibo(num))