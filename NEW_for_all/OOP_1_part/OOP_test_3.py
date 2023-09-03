# __<имя магического метода>__
# __init(self)__инициализатор объекта класса
# __del(self)__ финализатор класса

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        print('Вызов __init__')
        self.x = x
        self.y = y


    def __del__(self):
        print('Удаление экземпляра:' +str(self))


    def set_coords(self, x, y):
        self.x = x
        self.y = y


    def get_coords(self):
        return (self.x, self.y)
    
pt = Point(4, 5)
print(pt.__dict__)
# ссылка на созданный экземпляр класса
# ------ПРИМЕЧАНИЕ-------
# 1) создается объект (метод __new__)
# 2)инициализация объекта __init__