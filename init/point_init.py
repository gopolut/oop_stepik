class Point:
    # СБОРЩИК МУСОРА - это алгоритм, который удаляет объект из памяти,
    # когда на него больше нет ни одной ссылки

    # функция внутри класса называется метод
    def __init__(self, x=1, y=0):
        print('вызов __init__')
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        # self - это ссылка на объект экземпляра класса
        self.x = x
        self.y = y
        print('coordinates: ',self.x, self.y, self)

    def get_coord(self):
        return (self.x, self.y)

if __name__ == '__main__':
    pt = Point()
    print(pt.__dict__)
