import pytest
from seminar14 import *


@pytest.fixture
def data():
    a = Matrix(matrix_creator(5, 5))
    b = Matrix(matrix_creator(5, 5))
    c = Matrix(matrix_creator(4, 4))
    t1 = Triangle((5, 4, 5))
    t2 = Triangle((5, 5, 5))
    t3 = Triangle((1, 4, 2))
    return [a, b, c, t1, t2, t3]


def test_LessEqualZeroError(data):
    assert Matrix(matrix_creator(5, 5))


def test_TypeError_add(data):
    assert data[0] + data[1]


#
def test_TypeError_sub(data):
    assert data[0] - data[1]


def test_TypeError_mul(data):
    assert data[0] * data[1]


#
def test_MatrixEq(data):
    assert data[0] == data[0]


#
def test_MatrixNotEq(data):
    assert data[0] != data[2]


def test_InstanceCreateError():
    Spruce(10)


def test_LessEqualZeroTr():
    with pytest.raises(LessEqualZeroError):
        Triangle((0, 0, 0))


def test_iso_triangle(data):
    assert (data[3].analyzer(), 'Треугольник равнобедренный.\n')


def test_eq_triangle(data):
    assert (data[4].analyzer(), 'Треугольник равносторонний.\n')


def test_not_exist_triangle(data):
    assert (data[5].analyzer(), 'Треугольник не существует.\n')


if __name__ == '__test_pytest__':
    pytest.main()
