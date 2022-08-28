# 1.5 Большой подвиг 100
# Основа для игры в минера

from random import randint


class Cell:
    def __init__(self, around_mines: int=0, mine: bool=0):
        self.around_mines = around_mines  # число мин вокруг данной клетки поля
        self.mine = mine  # наличие мины в текущей клетке
        self.fl_open = True  # открыта/закрыта клетка - булево значение,
                             # если True, то будут отображены клетки при выводе в функции show()


class GamePole:
    pole = []  # двумерный список N x N элементов

    def __init__(self, N, M):
        self.N = N  # размер поля
        self.M = M  # общее число мин на поле

        # TODO: формирование двумерных списков:
        #  [[3 for num in range(self.N)] for num in range(self.N)]
        # формируем поле
        self.pole = [[Cell() for n in range(self.N)] for n in range(self.N)]
        self.place_mines()
        self.mines_around()

    # создаем игровое поле (двумерный массив)
    # def fill(self):
    #     self.pole = ['#'] * self.N
    #     for i in range(self.N):
    #         self.pole[i] = ['#'] * self.N
    #
    # # заполняем поле ячейками без мин
    # def place_cells(self):
    #     for i in self.pole:
    #         for j in range(len(i)):
    #             i[j] = Cell()

    # размещаем мины в случайном порядке
    def place_mines(self):
        for i in range(self.M):
            # r = True
            while True:
                row = randint(0, self.N - 1)
                mine_in_cell = randint(0, self.N - 1)
                if self.pole[row][mine_in_cell].mine != 1:
                    self.pole[row][mine_in_cell].mine = 1
                    # r = False
                    break

    # определяем число мин вокруг клетки
    def mines_around(self):
        count_mines = 0  # для подсчета кол-ва мин вокруг ячейки
        for row in range(len(self.pole)):
            for j in range(len(self.pole[row])):
                if self.pole[row][j].mine != 1:
                    # проверяем ячейку слева
                    if j > 0:
                        if self.pole[row][j - 1].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку справа
                    if j < self.N - 1:
                        if self.pole[row][j + 1].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку сверху
                    if row > 0:
                        if self.pole[row - 1][j].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку снизу
                    if row < self.N -1:
                        if self.pole[row + 1][j].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку по диагонали сверху слева
                    if row > 0 and j > 0:
                        if self.pole[row - 1][j - 1].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку по диагонали сверху справа
                    if row > 0 and j < self.N - 1:
                        if self.pole[row - 1][j + 1].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку по диагонали снизу слева
                    if row < self.N - 1 and j > 0:
                        if self.pole[row + 1][j - 1].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                    # проверяем ячейку по диагонали снизу справа
                    if row < self.N - 1 and j < self.N - 1:
                        if self.pole[row + 1][j + 1].mine == 1:
                            count_mines += 1
                            self.pole[row][j].around_mines = count_mines
                count_mines = 0

    def show(self):
        # for row in self.pole:
        #     print(' '.join(['#' if not elem.mine else str('1') for elem in row]))
        #     print(' '.join([str(elem.fl_open) if isinstance(elem, Cell) else elem for elem in row]))

        # с помощью end=' '
        # print(cll.around_mines if cll.fl_open else "#", end=' ')
        # print('-------------------')
        # for row in self.pole:
        #     print(' '.join(['#' if not elem.fl_open else str(elem.around_mines) if not elem.mine else '*' for elem in row]))
        # print('-- то же самое с lambda --')
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


if __name__ == '__main__':
    N = 5
    M = 6
    pole_game = GamePole(N, M)
    pole_game2 = GamePole(3, 4)

    print(id(pole_game))
    print(id(pole_game2))

    # pole_game.show()
    # print('----------------')
    # pole_game2.show()

