 # 1.5 Подвиг 8.

class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        result = [f'{good.name}: {good.price}' for good in self.goods]  # вернет несколько строк
        # result = [', '.join(map(lambda x: f'{x.name}: {x.price}', self.goods))]  # вернет 1 строку
        print(len(result))
        return result

# TODO: в комментариях есть использование функции type(product_name, (cls,), {})
class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    cart = Cart()

    goods = {
        'tv1': TV('Samsung', 45000),
        'tv2':  TV('LG', 25000),
        'table1': Table('IKEA', 15000),
        'note1': Notebook('Apple', 60000),
        'note2': Notebook('Samsung', 30000),
        'cup1': Cup('tea_cup', 500),
    }
    for value in goods.values():
        cart.add(value)

    print(cart.get_list())
