import colorama
from colorama import Fore

colorama.init()
yell = Fore.YELLOW
red = Fore.RED
cyan = Fore.CYAN
reset = Fore.RESET


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
                print(red + "\nНеверный ввод!\n" + reset)
                continue
        except ValueError:
            print(red + "\nНеверный ввод! Введите число.\n" + reset)


def gross_than_zero(promt):
    x = 0
    while not x > 0:
        x = input_num(promt)
        if x == 0:
            print(yell + "\nЧисло должно быть больше нуля!\n" + reset)
        return x


############################################  Животные  ############################################

class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)

    def __str__(self):
        return f'Имя животного: {self.name}, возраст: {self.age}, голос: {self.voice}'


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')


class MeinGott:
    @staticmethod
    def tvar_create(class_type):
        match class_type.__name__:
            case 'Fish':
                return Fish('Nemo', 2, 'silver', 'bul-bul')
            case 'Dog':
                return Dog('Spark', 5, 'pitbull', 'bark!')
            case 'Raven':
                return Raven('Qarasique', 6, 'white', 'bravo!')


def animal_representer():
    fish = MeinGott.tvar_create(Fish)
    dog = MeinGott.tvar_create(Dog)
    bird = MeinGott.tvar_create(Raven)

    print('\nЗоопарк: ', yell)
    animals = [fish, dog, bird]
    for i in animals:
        print(i)

    print(reset, '\nГолоса животных: ', yell)
    animals = [fish, dog, bird]
    for i in animals:
        i.make_voice()

    print(reset, '\nПоведение животных: ', yell)
    fish.swim()
    dog.bark()
    bird.fly_around_corpse()
    print(reset)


############################################  Банкомат  ############################################

class Bankomat:
    def __init__(self,
                 bills=50,
                 min_duty=30,
                 duty_percent=1.5,
                 duty_limit=600,
                 cashback_percent=3,
                 overcash=5_000_000,
                 overcash_percent=10):
        self.__BILLS = bills
        self.__MIN_DUTY = min_duty
        self.__DUTY_PERCENT = duty_percent
        self.__DUTY_LIMIT = duty_limit
        self.__CASHBACK_PERCENT = cashback_percent
        self.__OVERCASH = overcash
        self.__OVERCASH_PERCENT = overcash_percent
        self._transaction_counter = 0
        self._duty = 0
        self._deposit = 0
        self.__menu = ''
        self._log_list = []

    def _tax(self):
        if self._deposit > self.__OVERCASH:
            self._deposit -= self._deposit * self.__OVERCASH_PERCENT / 100
            print(
                yell + 'НАЛОГ на роскошь' + reset + f'{round(self._deposit * self.__OVERCASH_PERCENT / 100)},'
                                                    f' сумма на счету {self._deposit}')
            self._log_list.append(-self._deposit * self.__OVERCASH_PERCENT / 100)

    def _cashback(self):
        self._tax()
        self._transaction_counter += 1
        if self._transaction_counter % 3 == 0 and self._transaction_counter != 0:
            self._deposit += self._deposit * self.__CASHBACK_PERCENT / 100
            print(
                yell + f'КЭШБЭК' + reset + f' на {round(self._deposit * self.__CASHBACK_PERCENT / 100)},'
                                           f' сумма на счету {self._deposit}')
            self._log_list.append(-self._deposit * self.__CASHBACK_PERCENT / 100)

    def _add_money(self):
        self._tax()
        input_money = 0
        while not (input_money > 0):
            input_money = int(input("Внесите купюру кратную 50: "))
            if input_money % self.__BILLS != 0 or input_money == 0:
                input_money = 0
                print(red + '\nКРАТНУЮ 50!' + reset)
                continue
            else:
                self._deposit += input_money
                print(
                    yell + f'\nБаланс пополнен' + reset + f' на {input_money},  сумма на счету {self._deposit}')
                self._log_list.append(input_money)
                self._cashback()

    def _take_money(self):
        input_money = 0
        while not (input_money > 0):
            input_money = input_num(
                yell + f'Сумма на счету равна ' + reset + f'{self._deposit} \nВведите сумму для снятия кратную 50: ')
            if input_money % self.__BILLS != 0 or input_money == 0:
                input_money = 0
                print(red + 'КРАТНУЮ 50!' + reset)
                continue
            else:
                if self._deposit < (input_money * self.__DUTY_PERCENT) or self._deposit < input_money + self.__MIN_DUTY:
                    print(
                        red + f'Недостаточно средств на счету для снятия,' + reset + f' сумма на счету {self._deposit}')
                else:
                    if input_money < input_money * self.__DUTY_PERCENT / 100:
                        self._deposit -= input_money
                        self._deposit -= self.__MIN_DUTY
                        self._duty += self.__MIN_DUTY
                        self._log_list.append(-(input_money + self.__DUTY_LIMIT))
                    elif input_money * self.__DUTY_PERCENT / 100 > self.__DUTY_LIMIT:
                        self._deposit -= input_money
                        self._deposit -= self.__DUTY_LIMIT
                        self._duty += self.__DUTY_LIMIT
                        print(
                            yell + f' Комиссия за снятие ' + reset + f'{self.__DUTY_LIMIT},'
                                                                     f' сумма на счету {self._deposit}')
                        self._log_list.append(-(input_money + self.__DUTY_LIMIT))
                    else:
                        self._deposit -= input_money
                        self._deposit -= input_money * self.__DUTY_PERCENT / 100
                        self._duty += input_money * self.__DUTY_PERCENT / 100
                        print(
                            yell + f' Комиссия за снятие ' + reset + f'{input_money * self.__DUTY_PERCENT / 100},'
                                                                     f' сумма на счету {self._deposit}')
                        self._log_list.append(-(input_money + self.__DUTY_PERCENT))
                    self._cashback()

    def _check_balance(self):
        print(f'Cумма на счету {self._deposit}')

    def _history(self):
        for i in self._log_list:
            round(i, 2)
            if i > 0:
                print(yell + f'Пополнение: ' + reset + f'{i}')
            if i < 0:
                print(yell + f'Снятие: ' + reset + f'{i}')

    def start_app(self):
        while True:
            menu = input_num(
                "\n 1. Пополнить.\n 2. Снять.\n 3. Баланс.\n 4. История операций.\n 0. Выход. \n\n" + cyan +
                "Введите номер операции: " + reset)
            print('\n')
            if not (0 <= menu < 5):
                menu = ''
                continue
            else:
                match menu:
                    case 1:
                        print(yell + 'Пополнение' + reset)
                        self._add_money()
                    case 2:
                        print(yell + 'Снятие' + reset)
                        self._take_money()
                    case 3:
                        print(yell + 'Баланс' + reset)
                        self._check_balance()
                    case 4:
                        print(yell + 'История операций' + reset)
                        self._history()
                    case 0:
                        print(cyan + 'Выход' + reset)
                        exit()


############################################  Ёлочка  ############################################

class Spruce:
    def __init__(self, rows=0):
        self.rows = rows
        self._space = ' '
        self._asterix = '*'

    def spruce_gen(self):
        while not self.rows > 0:
            self.rows = gross_than_zero('Сколько рядов у ёлочки? ')
        spaces = self.rows - 1
        stars = 1
        for i in range(self.rows):
            if i == 0:
                print(red + (self._space * spaces) + (self._asterix * stars) + (self._space * spaces) + reset)
            elif i % 2 == 0:
                print(yell + (self._space * spaces) + (self._asterix * stars) + (
                        self._space * spaces) + reset)
            else:
                print(
                    Fore.GREEN + (self._space * spaces) + (self._asterix * stars) + (self._space * spaces) + reset)
            stars += 2
            spaces -= 1


############################################  Треугольник  ############################################

class Triangle:
    def __init__(self):
        self.a = self.b = self.c = 0
        while not self.a > 0:
            self.a = gross_than_zero('Введите первую сторону: ')
        while not self.b > 0:
            self.b = gross_than_zero('Введите вторую сторону: ')
        while not self.c > 0:
            self.c = gross_than_zero('Введите третью сторону: ')
        self.__analizer()

    def __analizer(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if self.a == self.b == self.c:
                print(yell + "\nТреугольник равносторонний." + reset)
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                print(yell + "\nТреугольник равнобедренный, ", self.check_triangle() + reset)
            else:
                print(yell + "\nТреугольник ", self.check_triangle() + reset)
        else:
            print(yell + "\nТреугольник не существует.\n" + reset)

    def check_triangle(self):
        if (self.c ** 2 == self.a ** 2 + self.b ** 2) or (self.a ** 2 == self.b ** 2 + self.c ** 2) or (
                self.b ** 2 == self.a ** 2 + self.c ** 2):
            return yell + "прямоугольный.\n"
        elif (self.c ** 2 < self.a ** 2 + self.b ** 2) or (self.a ** 2 < self.b ** 2 + self.c ** 2) or (
                self.b ** 2 < self.a ** 2 + self.c ** 2):
            return yell + "остроугольный.\n"
        elif (self.c ** 2 > self.a ** 2 + self.b ** 2) or (self.a ** 2 > self.b ** 2 + self.c ** 2) or (
                self.b ** 2 > self.a ** 2 + self.c ** 2):
            return yell + "тупоугольный.\n"


while True:
    print("\n1. Фабрика животных\n"
          "2. Банкомат.\n"
          "3. Ёлочка\n"
          "4. Треугольник\n")
    ex_number = input_num(cyan + "Введите номер задачи от 1 до 4. Для выхода нажмите 0.  " + reset)
    if 5 >= ex_number >= 0:
        match ex_number:
            case 1:
                animal_representer()
            case 2:
                Bankomat().start_app()
            case 3:
                Spruce().spruce_gen()
            case 4:
                Triangle()
            case 0:
                exit(0)
    else:
        print(yell + "\nНеверный ввод! Введите номер задачи из списка.\n" + reset)








