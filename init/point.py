# 1.5. Подвиг 3

class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


if __name__ == '__main__':
    points = []
    for num in range(0, 2000, 2):
        points.append(Point(num, num))

    points[2].color = 'yellow'
    print(points[2].color)

# 2 вариант ============
# points = [Point(i, i, 'yellow') if i == 3 else Point(i, i)  for i in range(1,2000,2)]
# points = [Point(i, i) if i != 3 else Point(i, i, 'yellow') for i in range(1, 2000, 2)]

    for i in range(1, 2000, 2):
        if i == 3:
            points.append(Point(i, i, color='yellow'))
        else:
            points.append(Point(i, i))
