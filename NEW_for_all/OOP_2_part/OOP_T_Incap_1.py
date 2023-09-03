import os
os.system('clear')

class Point:

    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y


    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами!')


    def get_coord(self):
        return self.__x, self.__y
    
# _attribute -> режим доступа protected. Внутри и в дочерних классах
# __attribute -> режим private. Только внутри класса
# в Python сигнализирует, но никак не ограничивает доступ из вне
# dir() -> посмотреть все свойства

pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
# print(pt.__x, pt.__y)

# setter и getter интерфейсные методы для работы с private аттрибутами
# модуль accessify помогает дополнительно защитить  from accessify import private, protected