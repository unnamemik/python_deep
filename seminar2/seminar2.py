import math
import fractions
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


############################################  Задачи с семинара  ############################################

def bankomat():
    menu = ''
    BILLS = 50
    MIN_DUTY = 30
    DUTY_PERCENT = 1.5
    DUTY_LIMIT = 600
    CASHBACK_PERCENT = 3
    OVERCASH = 5_000_000
    OVERCASH_PERCENT = 10

    transaction_counter = 0
    duty = 0
    deposit = 0

    def tax():
        global deposit
        if deposit > OVERCASH:
            deposit -= deposit * OVERCASH_PERCENT / 100
            print(f'НАЛОГ на роскошь {round(deposit * OVERCASH_PERCENT / 100)},  сумма на счету {deposit}')

    def cashback():
        tax()
        global deposit, transaction_counter
        transaction_counter += 1
        if transaction_counter % 3 == 0 and transaction_counter != 0:
            deposit += deposit * CASHBACK_PERCENT / 100
            print(f'КЭШБЭК на {round(deposit * CASHBACK_PERCENT / 100)},  сумма на счету {deposit}')

    def add_money():
        tax()
        global deposit, transaction_counter
        input_money = 0
        while not (input_money > 0):
            input_money = input_num("Внесите купюру кратную 50: ")
            if input_money % BILLS != 0 or input_money == 0:
                input_money = 0
                print(Fore.YELLOW + 'Сумма должна быть кратна 50!' + Fore.RESET)
                continue
            else:
                deposit += input_money
                print(f'Баланс пополнен на {input_money},  сумма на счету {deposit}')
                cashback()

    def take_money():
        global deposit, duty, transaction_counter
        input_money = 0
        while not (input_money > 0):
            input_money = input_num(f"Сумма на счету равна {deposit} Введите сумму для снятия кратную 50: ")
            if input_money % BILLS != 0 or input_money == 0:
                input_money = 0
                print(Fore.YELLOW + 'Сумма должна быть кратна 50!' + Fore.RESET)
                continue
            else:
                if deposit < (input_money * DUTY_PERCENT) or deposit < input_money + MIN_DUTY:
                    print(Fore.YELLOW + f'Недостаточно средств на счету для снятия, сумма на счету {deposit}')
                else:
                    if input_money < MIN_DUTY / DUTY_PERCENT * 100:
                        print(MIN_DUTY / DUTY_PERCENT)
                        deposit -= input_money
                        deposit -= MIN_DUTY
                        duty += MIN_DUTY
                        print(f' Комиссия за снятие {MIN_DUTY}, сумма на счету {deposit}')
                    elif input_money * DUTY_PERCENT / 100 > DUTY_LIMIT:
                        deposit -= input_money
                        deposit -= DUTY_LIMIT
                        duty += DUTY_LIMIT
                        print(f' Комиссия за снятие {DUTY_LIMIT}, сумма на счету {deposit}')
                    else:
                        deposit -= input_money
                        deposit -= input_money * DUTY_PERCENT / 100
                        duty += input_money * DUTY_PERCENT / 100
                        print(f' Комиссия за снятие {input_money * DUTY_PERCENT / 100}, сумма на счету {deposit}')
                    cashback()

    def check_balance():
        print(f'Cумма на счету {deposit}')

    while True:
        menu = input(Fore.LIGHTGREEN_EX + "\n 1. Пополнить.\n 2. Снять.\n 3. Баланс.\n 0. Выход." + Fore.RESET
                     + "\n\nВведите номер оперции: ")
        print('\n')
        if not (0 <= int(menu) < 4):
            menu = ''
            continue
        else:
            match menu:
                case '1':
                    print('Пополнение')
                    add_money()
                case '2':
                    print('Снятие')
                    take_money()
                case '3':
                    print('Баланс')
                    check_balance()
                case '0':
                    print('Выход')
                    return


############################################  Hex конвертор  ############################################


def hex_convertor():
    BASE = 16
    n_inp = int(input('Введите число: '))
    res = ''
    n = n_inp

    while n > 0:
        if n % BASE < 10:
            res = str(n % BASE) + res
        else:
            match n % BASE:
                case 10:
                    res = res + 'a'
                case 11:
                    res = res + 'b'
                case 12:
                    res = res + 'c'
                case 13:
                    res = res + 'd'
                case 14:
                    res = res + 'e'
                case 15:
                    res = res + 'f'
        n = n // BASE

    print(Fore.YELLOW + 'Результат: ', res + Fore.RESET)
    print(Fore.YELLOW + 'Проверка hex(): ', hex(n_inp)[2:] + Fore.RESET)


############################################  Сложение и умножение дробей  ############################################
def fr_input(input_str):
    inp_str = ''
    while not inp_str:
        try:
            inp_str = (input(input_str)).split('/')
            numerator = int(inp_str[0])
            denominator = int(inp_str[1])
            if numerator == 0 or denominator == 0:
                print(Fore.RED + '\nОшибка! Числитель или знаменатель не должен быть равен нулю!\n' + Fore.RESET)
                inp_str = ''
                continue
            if numerator < 0 and denominator < 0:
                denominator = abs(denominator)
            fr_ = numerator, denominator
            return fr_
        except:
            print(Fore.RED + '\nЧислитель и знаменатель должны быть целыми числами!\n' + Fore.RESET)
            inp_str = ''


def lcm(a, b):
    a = abs(a)
    b = abs(b)
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def fr_reduce(a, b):
    res = ''
    fr_denominator = math.gcd(a, b)
    num = a // fr_denominator
    denom = b // fr_denominator
    if abs(num) == abs(denom):
        res = f' = {num // denom}'
    elif num == a and denom == b:
        res = f''
    else:
        res = f' = {num}/{denom}'
    return res


def fr_operations():
    numerator1, denominator1 = fr_input('Введите первую дробь в формате a/b: ')
    numerator2, denominator2 = fr_input('Введите вторую дробь в формате a/b: ')

    fr_denominator = lcm(denominator1, denominator2)
    fr_numerator = numerator1 * fr_denominator // denominator1 + numerator2 * fr_denominator // denominator2
    print(
        Fore.YELLOW + f'\nСложение: {numerator1}/{denominator1} + {numerator2}/{denominator2} = '
                      f'{fr_numerator}/{fr_denominator}{fr_reduce(fr_numerator, fr_denominator)}' + Fore.RESET)

    fr_numerator = numerator1 * numerator2
    fr_denominator = denominator1 * denominator2
    print(
        Fore.YELLOW + f'Умножение: {numerator1}/{denominator1} * {numerator2}/{denominator2} = '
                      f'{fr_numerator}/{fr_denominator}{fr_reduce(fr_numerator, fr_denominator)}' + Fore.RESET)

    f_1 = fractions.Fraction(numerator1, denominator1)
    f_2 = fractions.Fraction(numerator2, denominator2)
    print(Fore.YELLOW + '\nПроверка с fractions: {} + {} = {}'.format(f_1, f_2, f_1 + f_2) + Fore.RESET)
    print(Fore.YELLOW + 'Проверка с fractions: {} * {} = {}'.format(f_1, f_2, f_1 * f_2) + Fore.RESET)


############################################  Меню  ############################################


while True:
    print("\n1. Банкомат.\n"
          "2. Шестнадцатеричный конвертор.\n"
          "3. Сложение и умножение дробей.\n")
    ex_number = input_num(Fore.CYAN + "Введите номер задачи от 1 до 5. Для выхода нажмите 0.  " + Fore.RESET)
    if 3 >= ex_number >= 0:
        match ex_number:
            case 1:
                bankomat()
            case 2:
                hex_convertor()
            case 3:
                fr_operations()
            case 0:
                exit(0)
    else:
        print(Fore.YELLOW + "\nНеверный ввод! Введите номер задачи из списка.\n" + Fore.RESET)
