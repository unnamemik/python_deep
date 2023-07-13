import colorama
from colorama import Fore

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
def seminar_task():
    friend1 = ['Tom', ('t1', 't2', 't3', 't4', 't5', 't1', 't2', 't9')]
    friend2 = ['Ford', ('t1', 't2', 't7', 't8', 't5')]
    friend3 = ['Anton', ('t6', 't7', 't3', 't4', 't5')]

    things = {friend1[0]: friend1[1]}
    things.update({friend2[0]: friend2[1]})
    things.update({friend3[0]: friend3[1]})

    set1 = set(things['Tom'])
    set2 = set(things['Ford'])
    set3 = set(things['Anton'])

    union_set = set(set1 | set2 | set3)
    print(Fore.YELLOW, f'\nВсе вещи: ', {*union_set}, Fore.RESET)

    other_set = set()
    for key in things:
        for other_key in things:
            if other_key != key:
                other_set.update(set(things[other_key]))
        print(f'Уникальные вещи у {key} : {union_set - other_set}')
        other_set.clear()

    for key in things:
        print(Fore.YELLOW, f'У {key} нет вещей: {union_set ^ set(things[key])}', Fore.RESET)


############################################  Список дубликатов  ############################################
def double_finder():
    my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7]
    new_list = list({i for i in my_list if my_list.count(i) >= 2})
    print(' Исходный список: ', *my_list, '\n', Fore.YELLOW, 'Список дубликатов: ', *new_list, Fore.RESET)


############################################  Частые слова  ############################################
def gross_word():
    from pprint import pprint
    import wikipedia
    import re

    txt = wikipedia.summary('Che_Guevara')

    txt_clean = re.sub('[S\'„“,.—]', '', txt).lower().split()
    my_dict = dict({i: txt_clean.count(i) for i in txt_clean})

    pprint(sorted(my_dict.items(), key=lambda item: -item[1])[:10])


############################################  Рюкзак  ############################################
def mybackpack():
    import random
    from itertools import permutations

    backpack_weight = input_num('Сколько кг влезает в рюкзак? ')
    thing_max_weight = input_num('Сколько весит самая тяжелая вещь? ')

    def thing_generator(quant):
        return dict({'thing-' + str(i + 1): random.randint(1, thing_max_weight) for i in range(quant)})

    def backpack(things_set, max_weight):
        res_set = set()
        res_dict = dict()
        for i in range(len(things_set) + 1):
            things_variant = list(permutations(things_set.values(), i))
            if sum(things_variant[i]) <= max_weight:
                if sum(res_set) <= sum(things_variant[i]):
                    res_set.update(things_variant[i])
        for i in res_set:
            res_dict.update({tuple(key for key, value in set_name1.items() if value == i): i})
        return res_dict

    set_name1 = thing_generator(5)
    available_thing_list = backpack(set_name1, backpack_weight)

    print(Fore.YELLOW, f'У нас есть:', Fore.RESET)
    print(set_name1)
    print(Fore.YELLOW,
          f'\nВ рюкзак вместимостью {backpack_weight} влезут варианты (можно выбрать одну из вещей одинаковой массы):',
          Fore.RESET)
    print(*available_thing_list.items())


while True:
    print("\n1. Задание №8 - с семинара, предметы в рюкзаке - пересечение и вычитание множеств.\n"
          "2. Список дубликатов.\n"
          "3. Частые слова\n"
          "4. Рюкзак\n")
    ex_number = input_num(Fore.CYAN + "Введите номер задачи от 1 до 4. Для выхода нажмите 0.  " + Fore.RESET)
    if 5 >= ex_number >= 0:
        match ex_number:
            case 1:
                seminar_task()
            case 2:
                double_finder()
            case 3:
                gross_word()
            case 4:
                mybackpack()
            case 0:
                exit(0)
    else:
        print(Fore.YELLOW + "\nНеверный ввод! Введите номер задачи из списка.\n" + Fore.RESET)
