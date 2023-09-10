import os
from typing import Any
os.system('clear')
import math



#  магические методы пишутся через __<метод>__ (double underscope) => dunder

class Derivate:
    def __init__(self, func):
        self.__fn = func


    def __call__(self, x, dx = 0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx
    # вычисление производной функции
@Derivate
# Derivate выступает в качасте декоратора
def df_sin(x):
    return math.sin(x)

# Применяем класс Derivate  к нашей функции
# df_sin = Derivate(df_sin)
print(df_sin(math.pi / 4))



class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars


    def __call__(self, *args, **kwds):
        if not isinstance(args[0], str):
            raise TypeError
        else:
            return args[0].strip(self.__chars)
        

s1 = StripChars("!:; ?.,")
res = s1(' Hello World! ')
print(res)        


class Counter:
    def __init__(self):
        self.__counter = 0


    def __call__(self, step = 1, *args, **kwds):
        # print('__call__')
        self.__counter += step
        return self.__counter
    

c1 = Counter()
c2 = Counter()
# c1()
# c1(2)
# res1 = c1(10)
# res2 = c2(-5)
# print(res1, res2)
# классы которые можно вызывать => функторы

