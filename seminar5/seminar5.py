from os import path
from pprint import pprint
import colorama
from colorama import Fore

colorama.init()

############################################  Общие методы  ############################################
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

############################################  Путь к файлу  ############################################
def task_one():
    def file_tracker(file_path: str):
        return path.abspath(file_path), \
            path.basename(file_path).split('.')[0], \
            path.basename(file_path).split('.')[-1]

    print('\n', Fore.YELLOW, file_tracker('E:\\git\\python\\python_deep\\draft.py'), Fore.RESET)


############################################  Словарь с премиями ########################################
def task_two():
    names_list = ['вася', 'петя', 'зина', 'клава', 'олег']
    salary_list = [45000, 25000, 35000, 50000, 60000]
    premium_list = ['12.15%', '10.12%', '11.15%', '13.12%', '9.15%']
    def premium_calc(n_list, s_list, p_list):
        return dict({n_list[i]: (round(s_list[i] * float(p_list[i][:-1])) / 100) for i in range(len(n_list))})

    pprint(premium_calc(names_list, salary_list, premium_list))


############################################  Фибоначчи ############################################
def task_three(quant):
    def fibonacci(n):
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b

    for x in fibonacci(quant):
        print(Fore.YELLOW, x, Fore.RESET)


while True:
    print("\n1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. "
          "Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.\n"
          "2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: "
          "имена str, ставка int, премия str с указанием процентов вида «10.25%». \nВ результате получаем словарь "
          "с именем в качестве ключа и суммой премии в качестве значения. \nСумма рассчитывается как ставка умноженная "
          "на процент премии.\n"
          "3. Создайте функцию генератор чисел Фибоначчи\n")
    ex_number = input_num(Fore.CYAN + "Введите номер задачи от 1 до 3. Для выхода нажмите 0.  " + Fore.RESET)
    if 3 >= ex_number >= 0:
        match ex_number:
            case 1:
                task_one()
            case 2:
                task_two()
            case 3:
                task_three(input_num('Введите количество чисел: '))
            case 0:
                exit(0)
    else:
        print(Fore.YELLOW, "\nНеверный ввод! Введите номер задачи из списка.\n", Fore.RESET)
