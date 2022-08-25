class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        result = [number for number in self.data if self.LIMIT_Y[0] <= number <= self.LIMIT_Y[1]]
        print(*result)


graph_1 = Graph()
l = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
graph_1.set_data(l)
graph_1.draw()
