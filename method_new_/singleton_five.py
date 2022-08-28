# 1.6 Подвиг 7.
# Этот класс должен формировать только первые пять объектов.
# Остальные (шестой, и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

class SingletonFive:
    __instance = None
    __counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        print(cls.__counter)
        if cls.__counter <= 5:
            cls.__instance = super().__new__(cls)  # создаются новые объекты
        return cls.__instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    objs = [SingletonFive(str(n)) for n in range(10)]
    print('\n'.join(map(str, [id(name) for name in objs])))
    print('----------')
    print(type(objs[4]))
    print(type(objs[9]))

