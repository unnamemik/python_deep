import io
import unittest
from unittest.mock import patch
from seminar14 import *


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        class Other:
            def __init__(self, matrix):
                self.matrix = matrix

        self.a = Matrix(matrix_creator(5, 5))
        self.b = Matrix(matrix_creator(5, 5))
        self.c = Matrix(matrix_creator(4, 4))
        self.k = Other(matrix_creator(5, 5))

    def test_LessEqualZeroError(self):
        with self.assertRaises(LessEqualZeroError):
            Matrix(matrix_creator(0, 5))

    def test_TypeError_add(self):
        with self.assertRaises(TypeError):
            var = self.a + self.k

    def test_TypeError_sub(self):
        with self.assertRaises(TypeError):
            var = self.a - self.k

    def test_TypeError_mul(self):
        with self.assertRaises(TypeError):
            var = self.a * self.k

    def test_MatrixEq(self):
        self.assertEqual(self.a, self.a)

    def test_MatrixNotEq(self):
        self.assertNotEqual(self.a, self.c)


class TestSpruce(unittest.TestCase):
    def test_InstanceCreateError(self):
        self.spr = Spruce(10)


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.data = (3, 4, 5)
        self.t1 = Triangle((5, 4, 5))
        self.t2 = Triangle((5, 5, 5))
        self.t3 = Triangle((1, 4, 2))

    def test_LessEqualZeroError(self):
        self.tr = Triangle(self.data)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_iso_triangle(self, mock_stdout):
        print(self.t1.analyzer())
        self.assertEquals(mock_stdout.getvalue(), 'Треугольник равнобедренный.\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_eq_triangle(self, mock_stdout):
        print(self.t2.analyzer())
        self.assertEquals(mock_stdout.getvalue(), 'Треугольник равносторонний.\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_exist_triangle(self, mock_stdout):
        print(self.t3.analyzer())
        self.assertEquals(mock_stdout.getvalue(), 'Треугольник не существует.\n')


if __name__ == '__test_unittest__':
    unittest.main()
