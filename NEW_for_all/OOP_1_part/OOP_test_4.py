import os
os.system('clear')

class Point():

    # cls ссылается на текущий экз. класса -> Point (на сам класс)
    # self ссылается на создав экзю класса 
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для: ' + str(cls))
        return super().__new__(cls)
    # super() ссылка на базовый класс (Object)
    # в базовом классе и находится метод __new__(cls)

    def __init__(self, x = 0, y = 0):
        print('Вызов __init__ для: ' + str(self))
        self.x = x
        self.y = y


pt = Point(2, 3)

# Паттерн Singleton