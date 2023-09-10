import os
os.system('clear')




#  Через descriptor (шаблон)
class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом!")


    def __set_name__(self, owner, name):
        self.name = "_" + name


    def __get__(self, owner, instance):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)


    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        self.verify_coord(value)
        instance.__dict__[self.name] = value
        setattr(instance, self.name, value)
     


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # @classmethod
    # def verify_coord(cls, coord):
    #     if type(coord) != int:
    #         raise TypeError("Координата должна быть целым числом!")



p = Point3D(1, 2, 3)
print(p.__dict__)









#  -------- Неудобный метод для множества переменных 
# @property
# def x(self):
#     return self.x

# @x.setter
# def x(self, coord):
#     self.verify_coord(coord)
#     self._x = coord

# @property
# def y(self):
#     return self._y

# @y.setter
# def y(self, coord):
#     self.verify_coord(coord)
#     self._y = coord

# @property
# def x(self):
#     return self._z

# @x.setter
# def z(self, coord):
#     self.verify_coord(coord)
#     self._z = coord

# descriptor - класс содержащий маг метод __get__


# p = Point3D(1, 2, 3)
# print(p.__dict__) 