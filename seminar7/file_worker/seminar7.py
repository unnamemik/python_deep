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


if __name__ == "__main__":
    # makefile('mp3')
    # temp = {'mp3': 3, 'txt': 5, 'torrent': 2}
    # makefiles(**temp)
    rename_file(2, 'txt', 'txt', (2, 6), '_new_')
