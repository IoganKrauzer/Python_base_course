import os
from typing import Any
os.system('clear')


class Point:

    MAX_COORD = 100
    MIN_COORD = 0
    

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def ser_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # @classmethod
    # def set_bounce(cls, left):
    #     cls.MIN_COORD = left
    def __getattribute__(self, item):
        if item == 'y':
            raise ValueError('Доступ запрещен')
        else:
           return object.__getattribute__(self, item)
#  управляем обращением к аттрибутам

    def __setattr__(self, key, value):
        print('__setattr')
        if key == 'z':
            raise AttributeError('недопустимое имя аттрибута')
        else:
            # object.__setattr__(self, key, value)
        # дополнительная возможность
            self.__dict__[key] = value

    
    def __getattr__(self, item):
        print('__getattr__' + item)
        return False
    

    def __delattr__(self, item):
        print('__delattr__ + item')
        object.__delattr__(self, item)



pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.z)
del pt1.x
print(pt1.__dict__)
# pt1.x = 5
# print(pt1.x)
# a = pt1.x
# pt1.x = 5
# print(a)
# Point.set_bounce( -100)
# pt1.set_bounce(-100)
# print(pt1.__dict__)
# print(Point.MIN_COORD)


# магические методы для аттрибутов:
# 1. __setattr__(self, key, value) - автоматич/ при изменен свойства key класса
# 2. __getattribute__(self, item) - автоматич. при получен. свойств класса с именем item
# 3. __getattr__(self, item) - автоматич. вызывается при получен. несущ. свойства класса item
# 4. __delattr__(self, item) - автоматич. вызывается при удалении свойства item

