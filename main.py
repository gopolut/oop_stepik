print('hello, mother fucker!')
print('Это курс по ООП.')

class Point:
    color = 'red'
    circle = 2

if __name__ == '__main__':
    new_ex = Point()
    new_ex.color = 'black'
    new_ex.circle = 21

    print(getattr(new_ex, 'hui', 'net takogo atributa'))  # возвращает значение атрибута
    print(hasattr(new_ex, 'color'))  # проверяет наличие атрибута

    # присвоение нового атрибута
    setattr(new_ex, 'name', 'Big circle')
    setattr(new_ex, 'coordinates', (3, 6))
    new_ex.length = 26  # локальное свойство для объекта new_ex

    # удаление атрибута
    delattr(new_ex, 'coordinates')
    del new_ex.name  # удаляет атрибут в текущем пространстве имен
    print(hasattr(new_ex, 'name'))

    # атрибуты у конкретного экземпляра класса
    print('атрибуты: ', [val for val in new_ex.__dict__])