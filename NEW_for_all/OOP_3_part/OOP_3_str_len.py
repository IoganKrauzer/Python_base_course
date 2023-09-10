import os
os.system('clear')

class Cat:
    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f'{self.__class__}: {self.name}'
    # вывод для разработчика


    def __str__(self):
        return f'{self.name}'
    

# __repr__() вывод для разработчика
# __str__() вывод для пользователя 
cat = Cat('Vasya')    
# print(str(cat))
# print(cat.name)

# ------------------------------------__len__(); __abs__()


class Point:
    def __init__(self, *args):
        # произвольное ко-во координат
        self.__coords = args


    def __len__(self):
        return len(self.__coords)
    

    def __abs__(self):
        return list(map(abs, self.__coords))



pt = Point(1, 2, -5)
print(len(pt))
print(abs(pt))
