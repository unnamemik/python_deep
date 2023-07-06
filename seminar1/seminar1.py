import colorama
from colorama import Fore, Back

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


def grossZero(promt):
    x = 0
    while not x > 0:
        x = input_num(promt)
        if x == 0:
            print(Fore.YELLOW + "\nЧисло должно быть больше нуля!\n" + Fore.RESET)
        return x


############################################  Задачи с семинара  ############################################
def spruce():
    rows = 0
    space = ' '
    asterix = '*'
    while not rows > 0:
        rows = grossZero('Сколько рядов у ёлочки? ')
    spaces = rows - 1
    stars = 1
    for i in range(rows):
        if i == 0:
            print(Fore.RED + (space * spaces) + (asterix * stars) + (space * spaces) + Fore.RESET)
        elif i % 2 == 0:
            print(Fore.YELLOW + (space * spaces) + (asterix * stars) + (space * spaces) + Fore.RESET)
        else:
            print(Fore.GREEN + (space * spaces) + (asterix * stars) + (space * spaces) + Fore.RESET)
        stars += 2
        spaces -= 1


def multiTab():
    first_row = (2, 6)
    second_row = (6, 10)
    print('\nТаблица умножения')

    def printTab(row):
        for i in range(2, 11):
            for k in range(2, 6):
                print(Fore.GREEN + f'{k} * {i} ={i * k}\t', end='' + Fore.RESET)
            print('')
        print('\n')

    printTab(first_row)
    printTab(second_row)


############################################  Треугольник  ############################################
def triangle():
    a = b = c = 0
    while not a > 0:
        a = grossZero('Введите первую сторону: ')
    while not b > 0:
        b = grossZero('Введите вторую сторону: ')
    while not c > 0:
        c = grossZero('Введите третью сторону: ')

    def checkTriangle(a, b, c):
        if (c ** 2 == a ** 2 + b ** 2) or (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2):
            return (Fore.YELLOW + "прямоугольный.\n")
        elif (c ** 2 < a ** 2 + b ** 2) or (a ** 2 < b ** 2 + c ** 2) or (b ** 2 < a ** 2 + c ** 2):
            return (Fore.YELLOW + "остроугольный.\n")
        elif (c ** 2 > a ** 2 + b ** 2) or (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2):
            return (Fore.YELLOW + "тупоугольный.\n")

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print(Fore.YELLOW + "\nТреугольник равносторонний." + Fore.RESET)
        elif a == b or a == c or b == c:
            print(Fore.YELLOW + "\nТреугольник равнобедренный, ", checkTriangle(a, b, c) + Fore.RESET)
        else:
            print(Fore.YELLOW + "\nТреугольник ", checkTriangle(a, b, c) + Fore.RESET)
    else:
        print(Fore.YELLOW + "\nТреугольник не существует.\n" + Fore.RESET)


############################################  Простые числа  ############################################
def simpleDigits():
    num = 0
    while not num > 0:
        num = grossZero('Введите число от 2 до 100000: ')
        if num == 1 or num > 100000:
            print(Fore.YELLOW + "\nЧисло должно быть больше 1 и не больше 100000!\n" + Fore.RESET)
            num = 0
            continue

    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k = k + 1
    if k <= 0:
        print(Fore.YELLOW + f"\nЧисло {num} простое.\n" + Fore.RESET)
    else:
        print(Fore.YELLOW + f"\nЧисло {num} не является простым.\n" + Fore.RESET)


############################################  Угадай число  ############################################
def guessNum():
    from random import randint

    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000

    find_try = 10

    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    # print(num)      # cheats
    print('\nУгадай число от {0} до {1}.\n'.format(LOWER_LIMIT, UPPER_LIMIT))

    while find_try > 0:
        guess_try = input_num('Введи число: ')
        find_try -= 1
        if guess_try < num:
            print('У меня больше.')
        if guess_try > num:
            print('У меня меньше.')
        if guess_try == num:
            print(Fore.YELLOW + '\nТы угадал за {0} попыток! Число {1}.\n'.format(10 - find_try, num) + Fore.RESET)
    else:
        print(Fore.YELLOW + '\nНе угадал! Я загадал {0}.\n'.format(num) + Fore.RESET)


############################################  Меню  ############################################


while True:
    print("\n1. Задание №8 - с семинара, нарисовать в консоли ёлочку.\n"
          "2. Задание №9 - с семинара, таблица умножения.\n"
          "3. Треугольник\n"
          "4. Простые числа\n"
          "5. Угадай число\n")
    ex_number = input_num(Fore.CYAN + "Введите номер задачи от 1 до 5. Для выхода нажмите 0.  " + Fore.RESET)
    if 5 >= ex_number >= 0:
        match ex_number:
            case 1:
                spruce()
            case 2:
                multiTab()
            case 3:
                triangle()
            case 4:
                simpleDigits()
            case 5:
                guessNum()
            case 0:
                exit(0)
    else:
        print(Fore.YELLOW + "\nНеверный ввод! Введите номер задачи из списка.\n" + Fore.RESET)
