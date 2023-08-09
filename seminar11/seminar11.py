from random import randint
import colorama
import numpy as np
from colorama import Fore
from functools import total_ordering

colorama.init()


def input_num(x):
    check = True
    while check:
        try:
            number = int(input(x))
            if number >= 0:
                check = False
                return number
            else:
                print(Fore.RED + "\nНеверный ввод!\n" + Fore.RESET)
                continue
        except ValueError:
            print(Fore.RED + "\nНеверный ввод! Введите число.\n" + Fore.RESET)


def matrix_creator(row, column):
    _MIN_VAL = 1
    _MAX_VAL = 100
    matrix = list([[randint(_MIN_VAL, _MAX_VAL) for i in range(column)] for j in range(row)])
    return matrix


@total_ordering
class Matrix:
    """Операции с матрицами"""

    def __init__(self, matrix):
        """
        Инициализация экземпляра класса
        :param matrix: Матрица
        """
        self.matrix = matrix

    def __add__(self, other):
        """
        Сложение матриц
        :param other: Матрица
        :return: Сумма матриц
        """
        if np.shape(self.matrix) != np.shape(other.matrix):
            raise ValueError('Сложение матриц невозможно!')
        if isinstance(other, Matrix):
            return Matrix(np.add(self.matrix, other.matrix))
        return NotImplemented

    def __sub__(self, other):
        """
        Вычитание матриц
        :param other: Матрица
        :return: Разность матриц
        """
        if np.shape(self.matrix) != np.shape(other.matrix):
            raise ValueError('Вычитание матриц невозможно!')
        if isinstance(other, Matrix):
            return Matrix(np.subtract(self.matrix, other.matrix))
        return NotImplemented

    def __mul__(self, other):
        """
        Умножение матриц
        :param other: Матрица
        :return: Произведение матриц
        """
        if np.shape(self.matrix)[1] != np.shape(other.matrix)[0]:
            raise ValueError('Произведение матриц невозможно!')
        if isinstance(other, Matrix):
            return Matrix(np.dot(self.matrix, other.matrix))
        return NotImplemented

    def __str__(self):
        """
        Вывод на печать
        :param: Матрица
        """
        return f'Матрица: {self.matrix}'

    def __eq__(self, other):
        """
        Проверка на равенство
        :param: Матрица
        """
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return NotImplemented

    def __gt__(self, other):
        """
        Сравнение матриц
        :param: Матрица
        """
        if isinstance(other, Matrix):
            return self.matrix > other.matrix
        return NotImplemented


def processor():
    """
    Тестовый метод
    :return: Вывод в консоль
    """
    print(a := Matrix(matrix_creator(5, 5)))
    print(b := Matrix(matrix_creator(5, 5)))

    c = a + b
    d = a - b
    e = a * b

    print(Fore.YELLOW, '\nСумма матриц:', Fore.RESET, *c.matrix, sep='\n')
    print(Fore.YELLOW, '\nРазница матриц:', Fore.RESET, *d.matrix, sep='\n')
    print(Fore.YELLOW, '\nПроизведение матриц:', Fore.RESET, *e.matrix, sep='\n')

    print(Fore.YELLOW, '\nСравнение матриц:', Fore.RESET, '\na == b is', a == b)
    print('a > b is', a > b)
    print('a < b is', a < b)


processor()
