import csv
import json
import math
from random import randint


def csv_triple():
    quant = randint(100, 1000)
    with open('csv_triple.csv', 'w', newline='') as csv_file:
        head = ['a', 'b', 'c']
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(head)
        for _ in range(quant):
            writer.writerow([randint(-100, 100) for _ in range(3)])


def json_deco(func):
    def wrapper(*args, **kwargs):
        data = {}
        with open('answer.json') as f_read:
            try:
                data = json.load(f_read)
            except:
                pass
        with open('answer.json', 'w') as f_write:
            data.update({'args: ' + str(args): 'roots: ' + func(*args, **kwargs)})
            json.dump(data, f_write, indent=2)

    return wrapper


def quadreq_deco(func):
    def wrapper():
        csv_triple()
        with open('csv_triple.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            reader.__next__()
            for line in reader:
                a, b, c = map(int, line)
                func(a, b, c)

    return wrapper


@quadreq_deco
@json_deco
def quadreq(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0 and a != 0:
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 2)
        return f'x1 = {x1}, x2 = {x2}'
    elif discr == 0:
        x = round(-b / (2 * a), 2)
        return f'x = {x}'
    else:
        return 'NA'


if __name__ == '__main__':
    quadreq()
