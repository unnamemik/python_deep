from random import randint


def try_to_guess(lower_limit, upper_limit, find_try):
    """
    Угадайка - загадывает число.
    :param lower_limit: Нижняя граница
    :param upper_limit: Верхняя граница
    :param find_try: Число попыток
    :return: Результат и количество попыток
    """
    num = randint(lower_limit, upper_limit)
    print('Угадай число от {0} до {1}.\n'.format(lower_limit, upper_limit))
    tmp = find_try

    while find_try > 0:
        guess_try = int(input('Введи число: '))
        find_try -= 1
        if guess_try < num:
            print('У меня больше.')
        if guess_try > num:
            print('У меня меньше.')
        if guess_try == num:
            print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
    else:
        print(f'\nНе угадал! Я загадал {num}.')


if __name__ == '__main__':
    try_to_guess(1, 10, 5)
