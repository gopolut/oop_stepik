print('hello, mother fucker!')
print('Это курс по ООП.')

class Point:
    color = 'red'
    circle = 2

if __name__ == '__main__':
    new_ex = Point()
    new_ex.color = 'black'
    new_ex.circle = 21

    # получение атрибута
    print(getattr(new_ex, 'hui', 'net takogo atributa'))
    print(hasattr(new_ex, 'color'))

    # присвоение нового атрибута
    setattr(new_ex, 'name', 'Big circle')
    setattr(new_ex, 'coordinates', (3, 6))

    # удаление атрибута
    delattr(new_ex, 'coordinates')
    del new_ex.name
    print(hasattr(new_ex, 'name'))

print('атрибуты: ', [val for val in new_ex.__dict__])