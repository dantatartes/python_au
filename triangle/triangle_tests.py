import unittest
from triangle.triangle import Point, Triangle, TaskSolver


class TestPointAddMethod(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Point(2, 3) + Point(3, 3), (5, 6))
        self.assertEqual(Point(2.5, 3.0) + Point(1.2, 3.2), (3.7, 6.2))
        self.assertEqual(Point(-2, -3) + Point(2, 3), (0, 0))


class TestTriangleMethods(unittest.TestCase):
    def test_is_triangle(self):
        tr = Triangle(Point(0, 0), Point(0, 3), Point(4, 0))
        self.assertTrue(tr.is_triangle())

        tr = Triangle(Point(0, 0), Point(0, 3), Point(10, 0))
        self.assertTrue(tr.is_triangle())

        tr = Triangle(Point(0, 1.5), Point(3, 0), Point(1.5, 1))
        self.assertTrue(tr.is_triangle())

        tr = Triangle(Point(0, 1), Point(0, 3), Point(0, 6))
        self.assertFalse(tr.is_triangle())

        tr = Triangle(Point(0, 1.23), Point(0, 1.23), Point(0, 6))
        self.assertFalse(tr.is_triangle())

        tr = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))
        self.assertFalse(tr.is_triangle())

    def test_is_rb(self):
        tr = Triangle(Point(0, 0), Point(3, 0), Point(0, 3))
        self.assertTrue(tr.is_rb())

        tr = Triangle(Point(4.5, 4.5), Point(3, 0), Point(0, 3))
        self.assertTrue(tr.is_rb())

        tr = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))
        self.assertFalse(tr.is_rb())

        tr = Triangle(Point(0, 1.23), Point(0, 1.23), Point(0, 6))
        self.assertFalse(tr.is_rb())

        tr = Triangle(Point(0, 1), Point(0, 3), Point(0, 6))
        self.assertFalse(tr.is_rb())

    def test_square(self):
        tr = Triangle(Point(0, 1), Point(0, 3), Point(0, 6))
        self.assertEqual(tr.square(), -1)

        tr = Triangle(Point(0, 0), Point(3, 0), Point(0, 3))
        self.assertEqual(tr.square(), 4.5)

        tr = Triangle(Point(0, 0), Point(10.1, 0), Point(0, 10.1))
        self.assertEqual(tr.square(), 51.005)

        tr = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))
        self.assertEqual(tr.square(), -1)

        tr = Triangle(Point(0, 1.23), Point(0, 1.23), Point(0, 6))
        self.assertEqual(tr.square(), -1)

        tr = Triangle(Point(0, 1), Point(0, 3), Point(0, 6))
        self.assertEqual(tr.square(), -1)

    def test_str(self):
        tr = Triangle(Point(0, 0), Point(3, 0), Point(0, 3))
        self.assertEqual(str(tr), "0 0 3 0 0 3")


class TestTaskSolverMethods(unittest.TestCase):
    def test_parse_data(self):
        task_solver = TaskSolver('in.txt', 'out.txt')
        task_solver.read_data()
        self.assertEqual(task_solver.parse_data(), [[0, 3, 0, 4, 0, 0.07, ],
                                                    [0, 0, 0, 3, 3, 0]])

        task_solver = TaskSolver('in2.txt', 'out.txt')
        task_solver.read_data()
        self.assertEqual(task_solver.parse_data(), [[0.0, 0.0, 0.0, 6.0, 6.0, 0.0]])

    def test_find_largest_triangle(self):
        task_solver = TaskSolver('in.txt', 'out.txt')
        task_solver.read_data()
        task_solver.parse_data()
        self.assertEqual(task_solver.find_largest_triangle(), 4.5)

        task_solver = TaskSolver('in2.txt', 'out.txt')
        task_solver.read_data()
        task_solver.parse_data()
        self.assertEqual(task_solver.find_largest_triangle(), 18)

        task_solver = TaskSolver('in3.txt', 'out.txt')
        task_solver.read_data()
        task_solver.parse_data()
        self.assertEqual(task_solver.find_largest_triangle(), 0)


if __name__ == '__main__':
    unittest.main()