import csv
import json
import pickle
from colorama import Fore
import os
from string import ascii_letters
from random import randint, sample, randbytes


def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    """
    Создает указанное количество файлов, с заданным расширением и размером.
    :param extention: Расширение
    :param smallest: Диапазон имени, от
    :param largest: Диапазон имени, до
    :param min_bytes: Диапазон размера, от
    :param max_bytes: Диапазон размера, до
    :param count: Количество файлов
    :return: Созданный файл
    """
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))

    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


def makefiles(**extentions):
    """
    Создает заданное количество файлов по расширению
    :param extentions: Расширение
    :return: Файл
    """
    for extention, count in extentions.items():
        makefile(extention=extention, count=count)


def makefile_topath(path, extention):
    """
    Создает заданное количество файлов по расширению в указанном каталоге
    :param path: Путь
    :param extention: Расширение
    :return: Файл
    """
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    makefile(extention)


def replace_files():
    """
    Перемещает файлы в новую папку, по расширению файла
    :return: Перемещенный файл
    """
    for file in os.listdir():
        extention = file.split('.')[-1]
        if not os.path.exists(extention):
            os.mkdir(extention)
        os.replace(file, os.path.join(os.getcwd(), extention, file))


def rename_file(nums_quant: int, source_ext: str, dest_ext: str, diapazone: tuple, file_name=''):
    """
    Переименовывает файл, изменяя расширение, добавляя срез исходного имени, новое имя и счетчик.
    :param nums_quant: Разрядность счетчика
    :param source_ext: Исходное расширение
    :param dest_ext: Конечное расширение
    :param diapazone: Срез исходного имени
    :param file_name: Новое имя
    :return: Переименованный файл
    """
    start_diap, end_diap = diapazone
    counter = 10 ** (nums_quant - 1)
    for file in os.listdir():
        source_name = file.split('.')[0]
        if source_ext == file.split('.')[-1]:
            print(source_name[start_diap:end_diap])
            os.rename(file, source_name[start_diap:end_diap] + file_name + str(counter) + '.' + dest_ext)
            counter += 1


def file_listening(path='.'):
    """
    Рекурсивно обходит заданный каталог и все вложенные директории
    :param path: Путь
    :return: Результаты обхода сохраняются в файлы json, csv и pickle.
    """
    total_size = 0
    exp_dict = {}
    parent_dir = []
    child_dirs = []
    file_list = []
    dir_items = [parent_dir, child_dirs, file_list, total_size]

    for dirpath, dirnames, filenames in os.walk(path):
        current_size = 0
        dir_size = 0
        print(Fore.CYAN, '\nDirectory: ', dirpath, Fore.RESET)
        exp_dict.update({dirpath: dir_items})

        parent_path = dirpath.split('\\')[-2]
        print(Fore.RED, '\tParent directory: ', parent_path, Fore.RESET)
        dir_items[1].append('Parent directory: ' + parent_path)
        exp_dict.update({dirpath: dir_items})

        if dirnames:
            print(Fore.YELLOW, '\tChild directories: ', *dirnames, Fore.RESET)
            dir_items[1].append(['Child directories: '] + dirnames)
            exp_dict.update({dirpath: dir_items})

        if filenames:
            print('\t\tFiles:')
            dir_items[1].append('Files:')
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
                current_size += os.path.getsize(fp)
                dir_items[1].append(f'{f}, size = {current_size}b;')
                dir_items[3] = total_size
                exp_dict.update({dirpath: dir_items})
                print('\t\t', f, Fore.LIGHTGREEN_EX, 'size =', current_size, 'b', Fore.RESET)
                dir_size += current_size
            print(Fore.LIGHTGREEN_EX, f'\t\tDirectory size = {dir_size}', Fore.RESET)
            dir_items[2].append(f'Directory size = {dir_size}')
        dir_items = [[], [], [], []]
    print(Fore.LIGHTRED_EX, '\nTotal size: ', total_size, 'b', Fore.RESET)
    save_in_files(exp_dict)


def save_in_files(inp_data):
    with (open('json_file.json', 'a') as json_file,
          open('csv_file.csv', 'a') as csv_file,
          open('pickle_file.pickle', 'ab') as pickle_file):
        json.dump(inp_data, json_file, indent=2)

        head = inp_data.keys()
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(head)
        for key, values in inp_data.items():
            writer.writerow(values)

        pickle.dump(inp_data, pickle_file)


if __name__ == "__main__":
    # makefile('mp3')
    # temp = {'mp3': 3, 'txt': 5, 'torrent': 2}
    # makefiles(**temp)
    # rename_file(2, 'txt', 'txt', (2, 6), '_new_')
    file_listening(os.getcwd())
