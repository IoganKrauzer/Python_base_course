class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        # print('вызов метода set_coords' + str(self))
        # self ссылается на экземпляр из которого был вызван метод
        #  pt.set_coords == Point.set_coords(pt)
        self.x = x
        self.y = y

    
    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt_2 = Point()
# self подставляется автоматически
pt.set_coords(1, 2)
pt.get_coords()
print(pt.get_coords())
# print(pt.__dict__)
# pt_2.set_coords(11, 22)
# print(pt_2.__dict__)