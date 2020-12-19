import sys
from math import sqrt


class Point:
    __slots__ = "x", "y"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


class Triangle:
    __slots__ = "a_coords", "b_coords", "c_coords", "a", "b", "c"

    def __init__(self, a: Point, b: Point, c: Point):
        self.a_coords = a
        self.b_coords = b
        self.c_coords = c
        self.a = sqrt((b.x - c.x) * (b.x - c.x) + (b.y - c.y) * (b.y - c.y))
        self.b = sqrt((a.x - c.x) * (a.x - c.x) + (a.y - c.y) * (a.y - c.y))
        self.c = sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y))

    def __str__(self):
        return f"{self.a_coords.x} {self.a_coords.y} {self.b_coords.x} {self.b_coords.y} {self.c_coords.x} {self.c_coords.y}"

    def is_triangle(self):
        return (self.a < self.b + self.c) and (self.b < self.c + self.a) and (self.c < self.a + self.b)

    def is_rb(self):
        if self.is_triangle():
            return (self.a == self.b) or (self.b == self.c) or (self.c == self.a)
        return False

    def square(self):
        if self.is_triangle() and self.is_rb():
            p = (self.a + self.b + self.c) / 2
            s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
            return round(s, 3)
        return -1


class TaskSolver:
    __slots__ = "src", "dst", "raw_data", "data", "mx_square", "res_triangle"

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.raw_data = list()
        self.data = list()
        self.mx_square = 0
        self.res_triangle = None

    def read_data(self):
        with open(self.src) as f:
            self.raw_data = list(map(lambda x: x.strip('\n').split(), f.readlines()))
        return self.raw_data

    def parse_data(self):
        k = len(self.raw_data)
        for i in range(k):
            is_num_row = True
            if len(self.raw_data[i]) == 6:
                for j in range(6):
                    try:
                        self.raw_data[i][j] = float(self.raw_data[i][j])
                    except ValueError:
                        is_num_row = False
                if is_num_row:
                    self.data.append(self.raw_data[i])
        return self.data

    def find_largest_triangle(self):
        for line in self.data:
            triangle = Triangle(Point(line[0], line[1]),
                                Point(line[2], line[3]),
                                Point(line[4], line[5]))
            if triangle.square() > self.mx_square:
                self.mx_square = triangle.square()
                self.res_triangle = triangle
        return self.mx_square

    def write_data(self):
        with open(self.dst, 'w') as f:
            if self.mx_square != 0:
                f.write(str(self.res_triangle))
                return str(self.res_triangle)
            return 0


def main(src, dst):
    task_solver = TaskSolver(src, dst)
    task_solver.read_data()
    task_solver.parse_data()
    task_solver.find_largest_triangle()
    print(task_solver.res_triangle.square())
    task_solver.write_data()


if __name__ == "__main__":
    params = sys.argv
    main(params[1], params[2])
