import os
os.system('clear')

# __iter__(self) получение итератора для перебора объекта
# __next__(self) переход к следующему значению и его считывание


class FRange:

    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step


    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
#  итератор это объект у которого есть магический метод __next__() 
#  и магический метод __next__() вызывает функция next()


fr = FRange(0, 2, 0.5)
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())

for x in fr:
    print(x)
# не явно вызывает итератор, а потом с помощью next() перебирает


class FRange2:

    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    
    def __iter__(self):
        self.value = 0
        return self
    

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration
        


fr = FRange2(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()