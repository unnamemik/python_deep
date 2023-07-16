from random import randint
import colorama
from colorama import Fore, Back

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


# 1
def matrix_trans():
    MIN_VAL = 1
    MAX_VAL = 100
    row = input_num('Введите количество строк матрицы: ')
    column = input_num('Введите количество столбцов матрицы: ')
    matrix = list([[randint(MIN_VAL, MAX_VAL) for i in range(column)] for j in range(row)])
    print(Fore.YELLOW, '\nИсходная матрица:', Fore.RESET, *matrix, sep='\n')

    transposed = list(map(list, zip(*matrix)))

    print(Fore.YELLOW, '\nТранспонированная матрица:', Fore.RESET, *transposed, sep='\n')


# 2
def dict_change():
    def dict_convert(**kwargs):
        return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}

    inp_dict = {'123': 'fghj', '789': (13, 50), '910': ['sdf', 'jhg'], '456': 654}
    print('Исходный словарь: ', inp_dict)
    print(Fore.YELLOW, 'Новый словарь: ', dict_convert(**inp_dict), Fore.RESET)


# 3
def bankomat():
    BILLS = 50
    MIN_DUTY = 30
    DUTY_PERCENT = 1.5
    DUTY_LIMIT = 600
    CASHBACK_PERCENT = 3
    OVERCASH = 5_000_000
    OVERCASH_PERCENT = 10
    log_list = []

    transaction_counter = 0
    duty = 0
    deposit = 0
    menu = ''

    def tax():
        global deposit
        if deposit > OVERCASH:
            deposit -= deposit * OVERCASH_PERCENT / 100
            print(
                Fore.YELLOW + 'НАЛОГ на роскошь' + Fore.RESET + f'{round(deposit * OVERCASH_PERCENT / 100)},  сумма на счету {deposit}')
            log_list.append(-deposit * OVERCASH_PERCENT / 100)

    def cashback():
        tax()
        global deposit, transaction_counter
        transaction_counter += 1
        if transaction_counter % 3 == 0 and transaction_counter != 0:
            deposit += deposit * CASHBACK_PERCENT / 100
            print(
                Fore.YELLOW + f'КЭШБЭК' + Fore.RESET + f' на {round(deposit * CASHBACK_PERCENT / 100)},  сумма на счету {deposit}')
            log_list.append(-deposit * CASHBACK_PERCENT / 100)

    def add_money():
        tax()
        global deposit, transaction_counter
        input_money = 0
        while not (input_money > 0):
            input_money = input_num("Внесите купюру кратную 50: ")
            if input_money % BILLS != 0 or input_money == 0:
                input_money = 0
                print(Fore.RED + '\nКРАТНУЮ 50!' + Fore.RESET)
                continue
            else:
                deposit += input_money
                print(Fore.YELLOW + f'\nБаланс пополнен' + Fore.RESET + f' на {input_money},  сумма на счету {deposit}')
                log_list.append(input_money)
                cashback()

    def take_money():
        global deposit, duty, transaction_counter
        input_money = 0
        while not (input_money > 0):
            input_money = input_num(
                Fore.YELLOW + f'Сумма на счету равна ' + Fore.RESET + f'{deposit} \nВведите сумму для снятия кратную 50: ')
            if input_money % BILLS != 0 or input_money == 0:
                input_money = 0
                print(Fore.RED + 'КРАТНУЮ 50!' + Fore.RESET)
                continue
            else:
                if deposit < (input_money * DUTY_PERCENT) or deposit < input_money + MIN_DUTY:
                    print(
                        Fore.RED + f'Недостаточно средств на счету для снятия,' + Fore.RESET + f' сумма на счету {deposit}')
                else:
                    if input_money < MIN_DUTY / DUTY_PERCENT * 100:
                        print(MIN_DUTY / DUTY_PERCENT)
                        deposit -= input_money
                        deposit -= MIN_DUTY
                        duty += MIN_DUTY
                        print(
                            Fore.YELLOW + f' Комиссия за снятие ' + Fore.RESET + f'{MIN_DUTY}, сумма на счету {deposit}')
                        log_list.append(-(input_money + MIN_DUTY))
                    elif input_money * DUTY_PERCENT / 100 > DUTY_LIMIT:
                        deposit -= input_money
                        deposit -= DUTY_LIMIT
                        duty += DUTY_LIMIT
                        print(
                            Fore.YELLOW + f' Комиссия за снятие ' + Fore.RESET + f'{DUTY_LIMIT}, сумма на счету {deposit}')
                        log_list.append(-(input_money + DUTY_LIMIT))
                    else:
                        deposit -= input_money
                        deposit -= input_money * DUTY_PERCENT / 100
                        duty += input_money * DUTY_PERCENT / 100
                        print(
                            Fore.YELLOW + f' Комиссия за снятие ' + Fore.RESET + f'{input_money * DUTY_PERCENT / 100}, сумма на счету {deposit}')
                        log_list.append(-(input_money + DUTY_PERCENT))
                    cashback()

    def check_balance():
        print(f'Cумма на счету {deposit}')

    def history():
        for i in log_list:
            round(i, 2)
            if i > 0:
                print(Fore.YELLOW + f'Пополнение: ' + Fore.RESET + f'{i}')
            if i < 0:
                print(Fore.YELLOW + f'Снятие: ' + Fore.RESET + f'{i}')

    while True:
        menu = input_num(
            "\n 1. Пополнить.\n 2. Снять.\n 3. Баланс.\n 4. История операций.\n 0. Выход. \n\nВведите номер операции: ")
        print('\n')
        if not (0 <= menu < 5):
            menu = ''
            continue
        else:
            match menu:
                case 1:
                    print(Fore.YELLOW + 'Пополнение' + Fore.RESET)
                    add_money()
                case 2:
                    print(Fore.YELLOW + 'Снятие' + Fore.RESET)
                    take_money()
                case 3:
                    print(Fore.YELLOW + 'Баланс' + Fore.RESET)
                    check_balance()
                case 4:
                    print(Fore.YELLOW + 'История операций' + Fore.RESET)
                    history()
                case 0:
                    print(Fore.CYAN + 'Выход' + Fore.RESET)
                    exit()


while True:
    print("\n1. Транспонирование матрицы.\n"
          "2. Ключи и значения в словаре.\n"
          "3. Банкомат\n")
    ex_number = input_num(Fore.CYAN + "Введите номер задачи от 1 до 4. Для выхода нажмите 0.  " + Fore.RESET)
    if 3 >= ex_number >= 0:
        match ex_number:
            case 1:
                matrix_trans()
            case 2:
                dict_change()
            case 3:
                bankomat()
            case 0:
                exit(0)
    else:
        print(Fore.YELLOW + "\nНеверный ввод! Введите номер задачи из списка.\n" + Fore.RESET)
