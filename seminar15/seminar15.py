import argparse
import logging
from random import randint
import colorama
import numpy as np
from colorama import Fore
from functools import total_ordering

colorama.init()

yell = Fore.YELLOW
cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET


################################### Общие методы ##########################################

def matrix_creator(row, column):
    _MIN_VAL = 1
    _MAX_VAL = 100
    matrix = list([[randint(_MIN_VAL, _MAX_VAL) for i in range(column)] for j in range(row)])
    return matrix


################################### Классы-исключения ##########################################
logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')


class OperationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        logging.error(f'Операция невозможна! {self.value}\n')
        return f'Операция невозможна! {self.value}'


class LessEqualZeroError(Exception):
    def __init__(self, *value):
        self.value = value

    def __str__(self):
        logging.error(f'Значение должно быть больше нуля! {self.value}\n')
        return f'Значение должно быть больше нуля! {self.value}'


class InstanceCreateError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        logging.error(f'Экземпляр класса не создан! Ошибка ввода. {self.value}\n')
        return f'Экземпляр класса не создан! Ошибка ввода. {self.value}'


################################### Матрицы ##########################################
@total_ordering
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

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


def matrix_processor(args):
    if 0 in (args.m1r, args.m1c, args.m2r, args.m2c):
        raise LessEqualZeroError(args.m1r, args.m1c, args.m2r, args.m2c)

    a = Matrix(matrix_creator(args.m1r, args.m1c))
    logging.info(f'Матрица a: рядов {args.m1r}; столбцов {args.m1c}; {a}')
    b = Matrix(matrix_creator(args.m2r, args.m2c))
    logging.info(f'Матрица b: рядов {args.m2r}; столбцов {args.m2c}; {b}\n')

    c = a + b
    d = a - b
    e = a * b

    print(yell, '\nСумма матриц:', reset, *c.matrix, sep='\n')
    logging.info(f'Сумма матриц: {c}')
    print(yell, '\nРазница матриц:', reset, *d.matrix, sep='\n')
    logging.info(f'Разница матриц: {d}')
    print(yell, '\nПроизведение матриц:', reset, *e.matrix, sep='\n')
    logging.info(f'Произведение матриц: {e}\n')

    print(yell, '\nСравнение матриц:', reset, '\na == b is', a == b)
    logging.info(f'Сравнение матриц: a == b {a == b}')
    print('a > b is', a > b)
    logging.info(f'Сравнение матриц: a < b {a < b}')
    print('a < b is', a < b)
    logging.info(f'Сравнение матриц: a > b {a > b}\n')


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
                spruce.append(red + (self._space * spaces) + (self._asx * stars) + (self._space * spaces) + reset)
            elif i % 2 == 0:
                spruce.append(yell + (self._space * spaces) + (self._asx * stars) + (self._space * spaces) + reset)
            else:
                spruce.append(green + (self._space * spaces) + (self._asx * stars) + (self._space * spaces) + reset)
            stars += 2
            spaces -= 1
        spruce.append('\n')
        logging.info(f'Ёлочка: рядов {self.rows}\n')
        for line in spruce:
            logging.info(line)
        return spruce


def spruce_processor(inp_num):
    sp1 = Spruce(int(inp_num.rows))
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
        self.analyzer()

    def analyzer(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if self.a == self.b == self.c:
                return ("Треугольник равносторонний.",)
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return ("Треугольник равнобедренный, ", self.check_triangle())
            else:
                return ("Треугольник существует, ", self.check_triangle())
        else:
            return ("Треугольник не существует!",)

    def check_triangle(self):
        if (self.c ** 2 == self.a ** 2 + self.b ** 2) or (self.a ** 2 == self.b ** 2 + self.c ** 2) or (
                self.b ** 2 == self.a ** 2 + self.c ** 2):
            return ("прямоугольный.")
        elif (self.c ** 2 < self.a ** 2 + self.b ** 2) or (self.a ** 2 < self.b ** 2 + self.c ** 2) or (
                self.b ** 2 < self.a ** 2 + self.c ** 2):
            return ("остроугольный.")
        elif (self.c ** 2 > self.a ** 2 + self.b ** 2) or (self.a ** 2 > self.b ** 2 + self.c ** 2) or (
                self.b ** 2 > self.a ** 2 + self.c ** 2):
            return ("тупоугольный.")


def triangle_processor(args):
    a = args.a
    b = args.b
    c = args.c
    data = (a, b, c)
    t1 = Triangle(data)
    logging.info(f'Треугольник: {t1.analyzer()}, стороны: {a}, {b}, {c}.')
    print('\n', yell, *t1.analyzer(), reset, '\n')


######################################### Парсеры ############################################
# парсер верхнего уровня
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(description='Введите команду и аргументы:'
                                               ' | matrix_processor -m1r -m1c -m2r -m2c'
                                               ' | spruce_processor -rows'
                                               ' | triangle_processor -a -b -c')

# парсер для подкоманды 'matrix_processor'
parser_matrix = subparsers.add_parser(name='matrix_processor',
                                      help='Введите ряды и столбцы матриц через пробел. '
                                           '(e.g. python seminar15.py matrix_processor -m1r 5 -m1c 5 -m2r 5 -m2c 5)')
parser_matrix.add_argument('-m1r', type=int, default=5)
parser_matrix.add_argument('-m1c', type=int, default=5)
parser_matrix.add_argument('-m2r', type=int, default=5)
parser_matrix.add_argument('-m2c', type=int, default=5)
parser_matrix.set_defaults(func=matrix_processor)

# парсер для подкоманды 'spruce_processor'
parser_spruce = subparsers.add_parser(name='spruce_processor',
                                      help='Введите число рядов елочки. '
                                           '(e.g. python seminar15.py spruce_processor -rows 15)')
parser_spruce.add_argument('-rows', type=int, default=10)
parser_spruce.set_defaults(func=spruce_processor)

# парсер для подкоманды 'triangle_processor'
parser_triangle = subparsers.add_parser(name='triangle_processor',
                                        help='Введите стороны треугольника. '
                                             '(e.g. python seminar15.py triangle_processor -a 3 -b 4 -c 5)')
parser_triangle.add_argument('-a', type=int, default=3)
parser_triangle.add_argument('-b', type=int, default=4)
parser_triangle.add_argument('-c', type=int, default=5)
parser_triangle.set_defaults(func=triangle_processor)

args = parser.parse_args()
args.func(args)
