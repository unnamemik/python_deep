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
            print(f'{red}\nНеверный ввод! Введите число. ValueError {e}\n{reset}')


def matrix_creator(row, column):
    _MIN_VAL = 1
    _MAX_VAL = 100
    matrix = list([[randint(_MIN_VAL, _MAX_VAL) for i in range(column)] for j in range(row)])
    return matrix


################################### Классы-исключения ##########################################


class UserException(Exception):
    pass


class OperationError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Операция невозможна! {self.value}'


class LessEqualZeroError(UserException):
    def __init__(self, *value):
        self.value = value

    def __str__(self):
        return f'Значение должно быть больше нуля! {self.value}'


class InstanceCreateError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
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


def matrix_processor():
    m1r = input_num('Введите ряды первой матрицы: ')
    m1c = input_num('Введите столбцы первой матрицы: ')
    m2r = input_num('Введите ряды второй матрицы: ')
    m2c = input_num('Введите столбцы второй матрицы: ')

    if 0 in (m1r, m1c, m2r, m2c):
        raise LessEqualZeroError(m1r, m1c, m2r, m2c)

    print(a := Matrix(matrix_creator(m1r, m1c)))
    print(b := Matrix(matrix_creator(m2r, m2c)))

    c = a + b
    d = a - b
    e = a * b

    print(yell, '\nСумма матриц:', reset, *c.matrix, sep='\n')
    print(yell, '\nРазница матриц:', reset, *d.matrix, sep='\n')
    print(yell, '\nПроизведение матриц:', reset, *e.matrix, sep='\n')

    print(yell, '\nСравнение матриц:', reset, '\na == b is', a == b)
    print('a > b is', a > b)
    print('a < b is', a < b)


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
        return spruce


def spruce_processor():
    sp1 = Spruce(input_num('Сколько у ёлочки рядов? '))
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
                str_out = f'{yell}\nТреугольник равносторонний.{reset}'
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                str_out = f'{yell}\nТреугольник равнобедренный.{reset}'
            else:
                str_out = f'{yell}\nТреугольник не существует.\n{reset}'
        return str_out


def triangle_processor():
    a = input_num('Введите первую сторону: ')
    b = input_num('Введите вторую сторону: ')
    c = input_num('Введите третью сторону: ')
    data = (a, b, c)
    t1 = Triangle(data)
    print(t1.analyzer())


while True:
    print("\n1. Матрицы\n"
          "2. Ёлочка (LessThanZeroError)\n"
          "3. Треугольник\n")
    ex_number = input_num(cyan + "Введите номер задачи от 1 до 3. Для выхода нажмите 0.  " + reset)
    if 4 >= ex_number >= 0:
        match ex_number:
            case 1:
                matrix_processor()
            case 2:
                spruce_processor()
            case 3:
                triangle_processor()
            case 0:
                exit(0)
    else:
        print(yell + "\nНеверный ввод! Введите номер задачи из списка.\n" + reset)
