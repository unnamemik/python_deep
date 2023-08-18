from random import randint
import numpy as np
from functools import total_ordering


################################### Общие методы ##########################################

def input_num(x):
    check = True
    while check:
        try:
            number = int(input(x))
            if number >= 0:
                check = False
                return number
            else:
                continue
        except ValueError as e:
            print(f'\nНеверный ввод! Введите число. ValueError {e}\n')
def matrix_creator(row, column):
    _MIN_VAL = 1
    _MAX_VAL = 100
    matrix = list([[randint(_MIN_VAL, _MAX_VAL) for i in range(column)] for j in range(row)])
    return matrix


################################### Классы-исключения ##########################################


class OperationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Операция невозможна! {self.value}'


class LessEqualZeroError(Exception):
    def __init__(self, *value):
        self.value = value

    def __str__(self):
        return f'Значение должно быть больше нуля! {self.value}'


class InstanceCreateError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Экземпляр класса не создан! Ошибка ввода. {self.value}'


################################### Матрицы ##########################################
@total_ordering
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        if 0 in np.shape(matrix):
            raise LessEqualZeroError(matrix)

    def __add__(self, other):
        if np.shape(self.matrix) != np.shape(other.matrix):
            raise OperationError(np.shape(self.matrix) != np.shape(other.matrix))
        if isinstance(other, Matrix):
            return Matrix(np.add(self.matrix, other.matrix))
        return NotImplemented

    def __sub__(self, other):
        if np.shape(self.matrix) != np.shape(other.matrix):
            raise OperationError(np.shape(self.matrix) != np.shape(other.matrix))
        if isinstance(other, Matrix):
            return Matrix(np.subtract(self.matrix, other.matrix))
        return NotImplemented

    def __mul__(self, other):
        if np.shape(self.matrix)[1] != np.shape(other.matrix)[0]:
            raise OperationError(np.shape(self.matrix)[1] != np.shape(other.matrix)[0])
        if isinstance(other, Matrix):
            return Matrix(np.dot(self.matrix, other.matrix))
        return NotImplemented

    def __str__(self):
        return f'Матрица: {self.matrix}'

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Matrix):
            return self.matrix > other.matrix
        return NotImplemented


############################################  Ёлочка  ############################################

class Spruce:
    def __init__(self, rows=0):
        if not rows > 0:
            raise InstanceCreateError(rows)
        self.rows = rows
        self._space = ' '
        self._asx = '*'

    def spruce_gen(self):
        spaces = self.rows - 1
        stars = 1
        spruce = []
        for i in range(self.rows):
            if i == 0:
                spruce.append((self._space * spaces) + (self._asx * stars) + (self._space * spaces))
            elif i % 2 == 0:
                spruce.append((self._space * spaces) + (self._asx * stars) + (self._space * spaces))
            else:
                spruce.append((self._space * spaces) + (self._asx * stars) + (self._space * spaces))
            stars += 2
            spaces -= 1
        return spruce


def spruce_processor():
    sp1 = Spruce(10)
    data = sp1.spruce_gen()
    for line in data:
        print(line)


############################################  Треугольник  ############################################

class Triangle:
    def __init__(self, sides=None):
        self.sides = sides
        if isinstance(sides, tuple):
            self.a, self.b, self.c = self.sides
            if not self.a > 0 or not self.b > 0 or not self.c > 0 or len(sides) != 3:
                raise LessEqualZeroError(sides)
        else:
            raise NotImplementedError

    def analyzer(self):
        str_out = ''
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if self.a == self.b == self.c:
                str_out = 'Треугольник равносторонний.'
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                str_out = 'Треугольник равнобедренный.'
        else:
            str_out = 'Треугольник не существует.'
        return str_out

