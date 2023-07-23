import colorama
from colorama import Fore

colorama.init()


def input_int_num(input_str):
    inp_str = ''
    while not inp_str:
        try:
            inp_str = (input(input_str)).split()
            coord_v = int(inp_str[0])
            coord_h = int(inp_str[1])
            if not (9 > coord_v > 0 and 9 > coord_h > 0):
                print(Fore.RED + '\nОшибка!Неверный ввод!\n' + Fore.RESET)
                inp_str = ''
                continue
            return coord_h - 1, coord_v - 1
        except:
            print(Fore.RED + '\nЧисло должно быть целым!\n' + Fore.RESET)
            inp_str = ''


if __name__ == '__main__':
    pass
