import random
from copy import deepcopy
import colorama
from colorama import Fore
from mygames.user_input import input_int_num

colorama.init()

# __examp_field = [
#     ['⬜', '⬛', '⬜', '⬛', '⬜', '♕', '⬜', '⬛'],
#     ['⬛', '⬜', '⬛', '♕', '⬛', '⬜', '⬛', '⬜'],
#     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '♕', '⬛'],
#     ['♕', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
#     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '♕'],
#     ['⬛', '♕', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
#     ['⬜', '⬛', '⬜', '⬛', '♕', '⬛', '⬜', '⬛'],
#     ['⬛', '⬜', '♕', '⬜', '⬛', '⬜', '⬛', '⬜']
# ]

__empty_field = [
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜']
]

__QUEEN = '♕'


def print_field(field):
    for i in range(8):
        print(7 - i + 1, end='')
        for j in range(8):
            print('\t', field[i][j], end='')
        print()
    print('\n\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8')


def check_empty(field, figure):
    counter = 0
    for i in range(8):
        counter = field[i].count(figure)
    return False if counter == 0 else True


def check_straight(field, figure):
    trans_field = list(map(list, zip(*field)))
    for i in range(8):
        if field[i].count(figure) > 1 or trans_field[i].count(figure) > 1:
            return False
    return True


def check_diagonal(field, figure):
    l_cross_list = []
    r_cross_list = []
    j = 8
    k = 0
    while j > 1:
        for i in range(j):
            l_cross_list.append(field[i + k][i])
            r_cross_list.append(field[i][i + k])
        j -= 1
        k += 1
        if l_cross_list.count(figure) > 1 or r_cross_list.count(figure) > 1:
            return False
        l_cross_list.clear()
        r_cross_list.clear()
    return True


def check_all(field, figure):
    return check_empty(field, figure) \
        and check_straight(field, figure) \
        and check_diagonal(field, figure) \
        and check_diagonal(turn_field(field), figure)


def turn_field(field):
    rotated_field = deepcopy(field)
    for i in rotated_field:
        i.reverse()
    return rotated_field


def random_field(figure):
    rand_field = deepcopy(__empty_field)
    for i in range(8):
        rand_value = random.randint(0, 7)
        rand_field[i][rand_value] = figure
    return rand_field


def set_user_field():
    set_field = deepcopy(__empty_field)
    ferz_list = ['первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого', 'седьмого', 'восьмого']
    counter = 0
    while counter < 8:
        coord_h, coord_v = input_int_num(f'Введите координаты {ferz_list[counter]} ферзя в числах через пробел (a b): ')
        set_field[coord_v][coord_h] = __QUEEN
        counter += 1
    set_field = list(map(list, zip(*turn_field(set_field))))
    print(Fore.YELLOW, 'Комбинация пользователя: ', Fore.RESET)
    print_field(set_field)
    print(check_all(set_field, __QUEEN))


def set_random_field():
    counter = 4
    while counter > 0:
        rand_field = random_field(__QUEEN)
        if check_all(rand_field, __QUEEN):
            print(Fore.YELLOW, f'\nСлучайная комбинация №{5 - counter}: ', Fore.RESET)
            print_field(rand_field)
            counter -= 1


if __name__ == '__main__':
    set_random_field()
