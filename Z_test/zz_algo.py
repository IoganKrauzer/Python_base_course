# from decimal import Decimal
import math
num = 1.26
print(math.floor(num))
# num = Decimal(str(num))
# print(num - int(num))
# print(num)

# Task_24
# kustov = int(input('Сколько кустов ты посадил ? '))
# urojai = [ random.randint(0,9) for i in range(kustov)]
# print(urojai)
# zadacha_roboty = int(input('С какого куста собрать ягоды? так же робот соберет и с соседних кустов тоже =) '))
# robot = 0
# if zadacha_roboty+1 > len(urojai):
#     robot += urojai[0] + urojai[zadacha_roboty-1] + urojai[zadacha_roboty-2]
# else:
#     robot += urojai[zadacha_roboty-2] + urojai[zadacha_roboty-1] + urojai[zadacha_roboty+1]
# print(robot)


# n = int(input('кол-во элементов первого множества ?'))nMassiv = [(int(input(f'{i} - элемент ?'))) for i in range(n)]
# m = int(input('кол-во элементов второго множества ?'))mMassiv = [(int(input(f'{j} - элемент ?'))) for j in range(m)]
# print(sorted(list(set(nMassiv+mMassiv))))