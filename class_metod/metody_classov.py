class Point:

    def set_coord(self, x, y):
        # self - это ссылка на объект экземпляра класса
        self.x = x
        self.y = y
        print('coordinates: ',self.x, self.y, self)

    def get_coord(self):
        return (self.x, self.y)


pt = Point()

# эти две записи эквивалентны
print('Point: ', Point.set_coord(pt, 33, 66))
pt.set_coord(3, 43)

# имена методов классов те же самые атрибуты
metod = getattr(pt, 'get_coord')
print(metod)  # ссылка на связанный метод с классом Point в RAM
print(metod())  # вызов самого метода конкретного экземпляра класса

