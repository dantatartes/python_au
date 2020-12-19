import unittest
from hexadecimal.hex import Node, HexNumber, Solution


class TestHexNumber(unittest.TestCase):
    def test_str(self):
        test_num = HexNumber("1FF")
        self.assertEqual(str(test_num), "1FF")

        test_num = HexNumber("1")
        self.assertEqual(str(test_num), "1")

        test_num = HexNumber("")
        self.assertEqual(str(test_num), "")

        test_num = HexNumber("AFF")
        self.assertEqual(str(test_num), "AFF")

        test_num = HexNumber("123")
        self.assertEqual(str(test_num), "123")

        with self.assertRaises(ValueError):
            test_num = HexNumber("fd")

        with self.assertRaises(ValueError):
            test_num = HexNumber("12f")

        with self.assertRaises(ValueError):
            test_num = HexNumber("Fad")


class TestSolution(unittest.TestCase):
    def test_str_to_num(self):
        first, second = HexNumber('1F'), HexNumber('A')
        test_sol = Solution(first, second)

        self.assertEqual(test_sol.str_to_num('1'), 1)
        self.assertEqual(test_sol.str_to_num('A'), 10)
        self.assertEqual(test_sol.str_to_num('F'), 15)

    def test_num_to_str(self):
        first, second = HexNumber('1F'), HexNumber('A')
        test_sol = Solution(first, second)

        self.assertEqual(test_sol.num_to_str(1), "1")
        self.assertEqual(test_sol.num_to_str(10), "A")
        self.assertEqual(test_sol.num_to_str(15), "F")

    def test_add(self):
        first, second = HexNumber('1F'), HexNumber('A')
        test_sol = Solution(first, second)
        test_sol.add()
        self.assertEqual(str(test_sol.result), '29')

        first, second = HexNumber('1F'), HexNumber('FF')
        test_sol = Solution(first, second)
        test_sol.add()
        self.assertEqual(str(test_sol.result), '11E')

        first, second = HexNumber('1'), HexNumber('1')
        test_sol = Solution(first, second)
        test_sol.add()
        self.assertEqual(str(test_sol.result), '2')

        first, second = HexNumber('1'), HexNumber('F')
        test_sol = Solution(first, second)
        test_sol.add()
        self.assertEqual(str(test_sol.result), '10')