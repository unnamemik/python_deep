import colorama
from colorama import Fore
import csv
from pprint import pprint

colorama.init()


class CheckName:
    def __init__(self, full_name=None, min_value=None, max_value=None):
        self.name_full = full_name
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not all(i.isalpha() for i in value.split()):
            raise TypeError(f'ФИО должны содержать только буквы!')
        if not value.istitle():
            raise ValueError(f'ФИО должны начинаться с заглавной буквы!')
        setattr(instance, self.param_name, value)


class Student:
    full_name = CheckName()

    def __init__(self, full_name):
        self.full_name = full_name
        self._student_grades = dict()
        self._student_tests = dict()
        self.subject_reader()

    def show_subjects(self):
        with open('lessons.csv', 'r', encoding='utf-8') as file:
            return csv.reader(file, delimiter=";").__next__()

    def subject_reader(self):
        with open('lessons.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=";")
            header = file_reader.__next__()
            for subj in header:
                self._student_grades.update({subj: []})
                self._student_tests.update({subj: []})

    def update_grades(self, subject, grade_val):
        if not 1 < grade_val < 6:
            raise ValueError('Оценки должны быть в диапазоне от 2 до 5!')
        new_val = self._student_grades[subject]
        new_val.append(grade_val)
        self._student_grades[subject] = new_val

    def update_tests(self, subject, test_val):
        if not -1 < test_val < 101:
            raise ValueError('Результаты тестов должны быть в диапазоне от 0 до 100!')
        new_val = self._student_tests[subject]
        new_val.append(test_val)
        self._student_tests[subject] = new_val

    def avg_subj_test(self, subject):
        res = 0
        counter = 0
        try:
            res += sum(self._student_tests[subject])
            counter += len(self._student_tests[subject])
            return round(res / counter, 2)
        except:
            return f'Результаты тестов отсутствуют!'

    def avg_grades(self):
        res = 0
        counter = 0
        try:
            for val in self._student_grades.values():
                if self._student_grades.values():
                    res += sum(val)
                    counter += len(val)
            return round(res / counter, 2)
        except:
            return f'Оценки отсутствуют!'

    def __str__(self):
        return f'\nФИО: {self.full_name}'

    def __repr__(self):
        return f'Student(full_name="{self.full_name}")'

    @property
    def grades_log(self):
        return self._student_grades

    @property
    def tests_log(self):
        return self._student_tests


if __name__ == '__main__':
    st1 = Student('Пантелеев Игнат Вольдемарович')
    print(st1.show_subjects())

    st1.update_grades('Математика', 5)
    st1.update_grades('Математика', 4)
    st1.update_grades('Математика', 5)

    st1.update_tests('Физика', 90)
    st1.update_tests('Физика', 80)
    st1.update_tests('Физика', 100)

    print(Fore.CYAN, st1, Fore.RESET)

    print(Fore.YELLOW, '\nЖурнал оценок:\n', Fore.RESET)
    pprint(st1.grades_log)
    print(Fore.YELLOW, '\nЖурнал результатов тестирования:\n', Fore.RESET)
    pprint(st1.tests_log)

    subj = 'Физика'
    print(Fore.YELLOW, '\nСредний балл студента по всем предметам = ', Fore.RESET, f'{st1.avg_grades()}')
    print(Fore.YELLOW, f'\nСредний результат тестов по предмету {subj} = ', Fore.RESET, f'{st1.avg_subj_test(subj)}')
