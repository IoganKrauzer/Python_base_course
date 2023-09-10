import os
os.system('clear')

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # используем, чтоб превратить в объект свойства property
    
    @property
    def old(self):
        return self.__old
    

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


    def get_old (self):
        return self.__old
    

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

    ol = property()
    ol = ol.setter(set_old)
    ol = ol.getter(get_old)



# p.__dict__['old'] = 'old in object p'
# .getter / .setter / .deleter  методы экземпляра класса property()
# Декораторы использовать при создании объекта свойства
# декораторы расширяют функционал другой функции


p = Person('Sergey', 20)
p.set_old(35)
print(p.get_old())

p.old = 34
print(p.old)
