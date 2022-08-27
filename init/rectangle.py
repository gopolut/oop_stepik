from random import randint, choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


if __name__ == '__main__':
    elements = []
    list_of_objects = {
        1: Line,
        2: Ellipse,
        3: Rect,
    }
    # TODO: магическая цифра, лучше значение присвоить переменной: count = 217
    # TODO: если переменная не используется в цикле, то лучше ее назвать '_'
    for _ in range(1, 17):
        elements.append(list_of_objects[randint(1, 3)](1, 2, 3, 4))

    # ПРИМЕР:
    # figure = choice([Line, Rect, Ellipse])

    # coords = [0, 0, 0, 0] if figure is Line else [randint(0, 100) for _ in range(4)]
    # elements.append(figure(*coords))

    # ПРИМЕР: использована функция для рандомной генерации choice():
    # elements = [choice(cls)(*sample(range(10), 4)) for _ in range(217)]

    for item in elements:
        if isinstance(item, Line):
            item.ep = (0, 0)
            item.sp = (0, 0)

    # ПРИМЕР:
    # elements = [Line(0, 0, 0, 0) if isinstance(item, Line) else item for item in elements]

    print(elements[3].__class__.__name__)

# 2 вариант =========
for i in range(217):
    rand_int = randint(1, 3)
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)
    d = randint(1, 100)
    if rand_int == 2:
        elements.append(list_of_objects[rand_int](0, 0, 0, 0))
    else:
        elements.append(list_of_objects[rand_int](a, b, c, d))
