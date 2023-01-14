from tkinter.messagebox import NO
import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class TestSquareRoot(unittest.TestCase):
    def test_square_root_returns_result(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(100), 10)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(13.5), 3.6742346141747673)

    def test_square_root_returns_float(self):
        self.assertIsInstance(square_root(4), float)

    def test_square_root_receives_string_returns_result(self):
        self.assertEqual(square_root('25'), 5)

    def test_square_root_without_arg_returns_exception(self):
        with self.assertRaises(TypeError):
            square_root()

    def test_square_root_receives_alpha_string_returns_zero(self):
        self.assertEqual(square_root('sdhgk25'), 0)


class TestQuadraticEquation(unittest.TestCase):
    def test_quadratic_equation_returns_result(self):
        self.assertEqual(quadratic_equation(1, -70, 600), (60, 10))
        self.assertEqual(quadratic_equation(3, -18, 27), (3, None))
        self.assertEqual(quadratic_equation(1, 4, 3), (-1, -3))
        self.assertEqual(quadratic_equation(1, 1, 1), (None, None))
        self.assertEqual(quadratic_equation(0, 1, 1), (None, None))
        self.assertEqual(quadratic_equation(1, 0, 1), (None, None))
        self.assertEqual(quadratic_equation(1, 1, 0), (0, -1))

    def test_quadratic_equation_returns_tuple(self):
        self.assertIsInstance(quadratic_equation(1, 4, 3), tuple)

    def test_quadratic_equation_receives_strings_returns_result(self):
        self.assertEqual(quadratic_equation('1', '4', '3'), (-1, -3))

    def test_quadratic_equation_receives_alpha_string_returns_none(self):
        self.assertEqual(quadratic_equation('dsgdsg', '4', '3'), (None, None))
        self.assertEqual(quadratic_equation('1', 'dsdhjjk', '3'), (None, None))
        self.assertEqual(quadratic_equation('dsgdsg', '4', 'fdhf'), (None, None))

    def test_quadratic_equation_without_arg_returns_exception(self):
        with self.assertRaises(TypeError):
            quadratic_equation()


class TestBubbleSort(unittest.TestCase):
    def test_buble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_buble_sort_single_item(self):
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([0]), [0])

    def test_buble_sort_two_item(self):
        self.assertEqual(bubble_sort([1, 2]), [1, 2])
        self.assertEqual(bubble_sort([0, -1]), [-1, 0])
        self.assertEqual(bubble_sort([0, 0]), [0, 0])

    def test_buble_sort_arger_integers(self):
        self.assertEqual(
            bubble_sort([135604, 1000000, 45, 78435, 456219832, 2, 546]), 
            [2, 45, 546, 78435, 135604, 1000000, 456219832]
            )



class TestShellSort(unittest.TestCase):
    def test_shell_sort_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_shell_sort_single_item(self):
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([0]), [0])

    def test_shell_sort_two_item(self):
        self.assertEqual(shell_sort([1, 2]), [1, 2])
        self.assertEqual(shell_sort([0, -1]), [-1, 0])
        self.assertEqual(shell_sort([0, 0]), [0, 0])

    def test_shell_sort_arger_integers(self):
        self.assertEqual(
            shell_sort([135604, 1000000, 45, 78435, 456219832, 2, 546]), 
            [2, 45, 546, 78435, 135604, 1000000, 456219832]
            )


if __name__ == '__main__':
    unittest.main()
