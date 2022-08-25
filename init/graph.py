class Graph:
    def __init__(self, data, is_show=True):
        #  каждого объекта должен быть свой список с данными,
        #  нужно создавать копию переданного списка
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def _show_closed(self):
        print('Отображение данных закрыто')

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            self._show_closed()

    def show_graph(self):
        if self.is_show:
            print('Графическое отображение данных:',*self.data)
            # print(' '.join(map(str, self.data)))
        else:
            self._show_closed()

    def show_bar(self) -> str:
        if self.is_show:
            print('Столбчатая диаграмма:',*self.data)
        else:
            self._show_closed()

    def set_show(self, fl_show):
        self.is_show = fl_show
        # if fl_show == True:
        #     self.is_show = True
        #     return True
        # else:
        #     self.is_show = False
        #     return False


if __name__ == '__main__':
    gr = Graph([3, 5 ,6, 1, 0])
    gr2 = Graph([1, 66, -32, 4])
    print(gr.is_show)

    gr.show_bar()
    gr.set_show(False)
    gr.show_table()
    gr.set_show(True)
    gr.show_graph()
    gr.show_bar()
    print('_________')
    gr2.set_show(True)
    gr2.show_bar()
