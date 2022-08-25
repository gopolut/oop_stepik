class TriangleChecker:
    def __init__(self, a, b, c):
        self.nums = [a, b, c]

    def is_triangle(self):

        # code 1
        for num in self.nums:
            # if type(num) != int and type(num) != float:
            if not type(num) in (int, float):
                return 1
            if num <= 0:
                return 1

        # codes 2
        sort = sorted(self.nums)
        if sort[0] + sort[1] < sort[2]:
            print('This is not a triangle!')
            return 2
        # codes 3
        else:
            print('It is a triangle')
            return 3


if __name__ == '__main__':
    tr = TriangleChecker(3, 4, 5)
    print(tr.is_triangle())


# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        nums = [self.a, self.b, self.c]
        # code 1
        for num in nums:
            # if type(num) != int and type(num) != float:
            if not type(num) in (int, float):
                return 1
            if num <= 0:
                return 1

        # codes 2
        sort = sorted(nums)
        if sort[0] + sort[1] < sort[2]:
            # print('This is triangle!')
            return 2
        # codes 3
        else:
            # print('Its not triangle')
            return 3

if __name__ == '__main__':
    a, b, c = map(int, input().split()) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
    tr = TriangleChecker(a, b, c)
    print(tr.is_triangle())