import doctest
from seminar14 import *


class Other:
    def __init__(self, matrix):
        self.matrix = matrix



def matrix_processor():
    """
    Operations with matrix
    >>> Matrix(matrix_creator(0, 5))
    Traceback (most recent call last):
    ...
    seminar14.LessEqualZeroError: Значение должно быть больше нуля! ([],)
    >>> Matrix(matrix_creator(5, 5)) + Other(matrix_creator(5, 5))
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'Matrix' and 'Other'
    >>> Matrix(matrix_creator(5, 5)) == Other(matrix_creator(5, 5))
    False
    >>> Matrix(matrix_creator(5, 5)) != Other(matrix_creator(5, 5))
    True
    >>> m1 = Matrix(matrix_creator(5, 5))
    >>> m1 == m1
    True
    """

def spruce_processor():
    """
    Spruce generator
    >>> Spruce(0)
    Traceback (most recent call last):
    ...
    seminar14.InstanceCreateError: Экземпляр класса не создан! Ошибка ввода. 0
    >>> Spruce('10')
    Traceback (most recent call last):
    ...
    TypeError: '>' not supported between instances of 'str' and 'int'
    """

def triangle_processor():
    """
    Triangle generator
    >>> Triangle((0, 0, 0))
    Traceback (most recent call last):
    ...
    seminar14.LessEqualZeroError: Значение должно быть больше нуля! ((0, 0, 0),)
    >>> Triangle((4, 5)).analyzer()
    Traceback (most recent call last):
    ...
    ValueError: not enough values to unpack (expected 3, got 2)
    >>> Triangle((1, 2, 3, 4)).analyzer()
    Traceback (most recent call last):
    ...
    ValueError: too many values to unpack (expected 3)
    >>> Triangle().analyzer()
    Traceback (most recent call last):
    ...
    NotImplementedError
    >>> print(Triangle((5, 4, 5)).analyzer())
    Треугольник равнобедренный.
    >>> print(Triangle((5, 5, 5)).analyzer())
    Треугольник равносторонний.
    >>> print(Triangle((1, 4, 2)).analyzer())
    Треугольник не существует.
    """

if __name__ == '__test_doctest__':
    doctest.testmod()
