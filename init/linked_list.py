# 1.5 Подвиг 9
# Односвязный список

class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

    def __str__(self):
        return f'cur obj: {self.data}, next: {self.next_obj.data}'


if __name__ == '__main__':
    lst_in = ['jopa', 34, 'govno', True]

    head_obj = ListObject(lst_in[0])
    obj = head_obj

    # TODO: если использовать срез, то будет создаваться его копия каждую итерацию цикла!
    for i in range(1, len(lst_in)):
        obj_new = ListObject(lst_in[i])
        obj.link(obj_new)
        obj = obj_new

        print(ListObject(lst_in[i]).__str__())

    # obj2 = ListObject(lst_in[1])
    # obj3 = ListObject(lst_in[2])
    # obj4 = ListObject(lst_in[3])
    #
    # head_obj.link(obj2)
    # obj2.link(obj3)
    # obj3.link(obj4)
    #
    # print(obj1.__str__())
    # print(obj2.__str__())
    # print(obj3.__str__())
    # print(obj4.__str__())
