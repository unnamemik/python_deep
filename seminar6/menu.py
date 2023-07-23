from mygames import check_date, try_to_guess, set_user_field, set_random_field
import colorama
from colorama import Fore

colorama.init()


def menu():
    while True:
        print("\n1. Проверка года на високосность.\n"
              "2. Угадайка.\n"
              "3. 8 ферзей - пользовательский режим.\n"
              "4. 8 ферзей - четыре случайных комбинации.\n")
        ex_number = int(input(Fore.CYAN + "Введите номер задачи от 1 до 4. Для выхода нажмите 0.  " + Fore.RESET))
        if 4 >= ex_number >= 0:
            match ex_number:
                case 1:
                    print(check_date(input('Введите дату в формате DD.MM.YYYY : ')))
                case 2:
                    try_to_guess(1, 10, 5)
                case 3:
                    set_user_field()
                case 4:
                    set_random_field()
                case 0:
                    exit(0)
        else:
            print(Fore.YELLOW + "\nНеверный ввод! Введите номер задачи из списка.\n" + Fore.RESET)


if __name__ == '__main__':
    menu()