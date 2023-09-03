import os
os.system('clear')
# setattr(Class, '<имя аттрибута>', его значение)
# getattr(Point, 'a', False) если нет такого аттрибута, то вернет false
# del Point.<наименование аттрибута> удаляет аттрибут
# hasattr(Point, '<имя аттрибута>') проверяет наличие аттрибута
# delattr(Point, '<имя аттриб>') удаляет аттрибут

class Point:
    color = 'red'
    circle = 2

# a.__dict__  перечень аттрибутов экземпляра
# a.__doc__ строка с описанием класса
a = Point()
b = Point()
a.x = 1
a.y = 2
# создание локальной переменной
b.x = 10
b.x = 20

