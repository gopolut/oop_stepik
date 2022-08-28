# 1.6 Магический метод __new__. Подвиг 6


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создавать объекты абстрактного класса' + str(cls)


if __name__ == '__main__':
    obj = AbstractClass()
    print(obj)
    print(id(obj))
    print(type(obj))