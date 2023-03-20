# TODO: Задание связанное с ПК
# Сделал Андрюша жи есть
# Класс Convert чисто чтобы из строки сделать число и прога не вылетела
# А всё остальное и так ясно, отладчик в помощь

class Convert:
    @staticmethod
    def string_to_int():
        while True:
            try:
                param = int(input())
            except (TypeError, ValueError) as err:
                print("Введите числовое значение")
            else:
                return param


class CPU:
    def __init__(self):
        self.name = input("Введите имя процессора:\t")
        print("Введите тактовую частоту")
        self.frequency = Convert.string_to_int()
        print("Введите количество ядер")
        self.nucleus = Convert.string_to_int()
        self.socket = input("Введите сокет процессора:\t")

    def info_cpu(self):
        print("** Процессор **")
        print(f"\tНазвание процессора: {self.name}")
        print(f"\tТактовая частота: {self.frequency}")
        print(f"\tКоличество ядер: {self.nucleus}")
        print(f"\tСокет: {self.socket}")


class GPU:
    def __init__(self):
        self.name = input("Введите имя видеокарты:\t")
        print("Введите тактовую частоту")
        self.frequency = Convert.string_to_int()
        print("Введите объём памяти")
        self.memory = Convert.string_to_int()

    def info_gpu(self):
        print("** Видеокарта **")
        print(f"\tНазвание видеокарты: {self.name}")
        print(f"\tТактовая частота: {self.frequency}")
        print(f"\tПамять: {self.memory}")


class RAM:
    def __init__(self):
        self.name = input("Введите имя ОЗУ:\t")
        print("Введите тактовую частоту")
        self.frequency = Convert.string_to_int()
        print("Введите количество модулей")
        self.numbermemory = Convert.string_to_int()
        print("Введите объём памяти одного модуля")
        self.memory = Convert.string_to_int()
        self.ddr = RAM.ddr_memory()

    def info_ram(self):
        print("** Оперативная память **")
        print(f"\tНазвание ОЗУ: {self.name}")
        print(f"\tТактовая частота: {self.frequency}")
        print(f"\tКоличество модулей: {self.numbermemory}")
        print(f"\tПамять одного модуля: {self.memory}")
        print(f"\tТип DDR: {self.ddr}")

    @staticmethod
    def ddr_memory():
        ddr_types = ["DDR", "DDR2", "DDR3", "DDR4", "DDR5"]
        print("Выберите тип DDR:\n"
              "1 - DDR\n"
              "2 - DDR2\n"
              "3 - DDR3\n"
              "4 - DDR4\n"
              "5 - DDR5")
        while True:
            try:
                indexDDR = Convert.string_to_int() - 1
                if (indexDDR > len(ddr_types) or indexDDR < 0):
                    raise TypeError
            except TypeError as err:
                print("Нет такого типа DDR")
            else:
                ddr = ddr_types[indexDDR]
                return ddr


class MotherBoard:
    def __init__(self):
        self.name = input("Введите название материнской платы:\t")
        self.socket = input("Введите сокет процессора:\t")
        self.ddrtypes = RAM.ddr_memory()
        print("Введите количество разъёмов для ОЗУ")
        self.maxram = Convert.string_to_int()
        self.cpu = None
        self.gpu = None
        self.ram = None

    def info_motherboard(self):
        print("** Материнская плата **")
        print(f"\t Название мат.платы: {self.name}")
        print(f"\t Сокет мат.платы: {self.socket}")
        print(f"\t Типы поддерживаемых RAM: {self.ddrtypes}")
        print(f"\t Максимальное количество RAM: {self.maxram}")
        if self.cpu is None:
            print(f"\t Процессор: Нет процессора")
        else:
            self.cpu.info_cpu()
        if self.gpu is None:
            print(f"\t Видеокарта: Нет видеокарты")
        else:
            self.gpu.info_gpu()
        if self.ram is None:
            print(f"\t Оперативная память: Нет ОЗУ")
        else:
            self.ram.info_ram()

    def insert_component(self):
        while True:
            print("Какой компонент вы хотите вставить?\n"
                  "\t1 - Процессор\n"
                  "\t2 - Видеокарта\n"
                  "\t3 - Оперативная память\n"
                  "\t4 - Ничего не вставлять")
            component = Convert.string_to_int()
            if component == 1:
                self.cpu = CPU()
                if self.socket == self.cpu.socket:
                    print("Процессор вставлен в плату")
                else:
                    print("Процессор не вставлен в плату")
                    print(f"Сокет мат.платы:\t {self.socket}")
                    print(f"Сокет процессора:\t {self.cpu.socket}")
                    self.cpu = None
            if component == 2:
                self.gpu = GPU()
                print("Видеокарта вставлена в плату")
            if component == 3:
                self.ram = RAM()
                if self.ddrtypes == self.ram.ddr:
                    if self.maxram == self.ram.numbermemory:
                        print("ОЗУ вставлена в плату")
                    else:
                        print("ОЗУ не вставлена в плату")
                        print(f"Всего разъёмов для ОЗУ на мат. плате:\t {self.maxram}")
                        print(f"Модулей памяти ОЗУ: {self.ram.numbermemory}")
                else:
                    print("ОЗУ не вставлена в плату")
                    print(f"Поддерживаемый DDR на мат.платы:\t {self.ddrtypes}")
                    print(f"DDR ОЗУ: {self.ram.ddr}")
                    self.ram = None
            if component == 4:
                break

    def del_component(self):
        while True:
            print("Какой компонент вы хотите удалить?\n"
                  "\t1 - Процессор\n"
                  "\t2 - Видеокарта\n"
                  "\t3 - Оперативная память\n"
                  "\t4 - Удалить всё\n"
                  "\t5 - Ничего не удалять")

            component = Convert.string_to_int()
            if component == 1:
                if self.cpu is None:
                    print("Нечего удалять :D")
                else:
                    print("Процессор удалён")
                    self.cpu = None
            elif component == 2:
                if self.gpu is None:
                    print("Нечего удалять :D")
                else:
                    print("Видеокарта удалена")
                    self.gpu = None
            elif component == 3:
                if self.ram is None:
                    print("Нечего удалять :D")
                else:
                    print("ОЗУ удалена")
                    self.ram = None
            elif component == 4:
                print("Компоненты удалены!")
                self.cpu = None
                self.gpu = None
                self.ram = None
            elif component == 5:
                break
            else:
                print("Такого компонента не существует!")


class PersonalComputer:
    def __init__(self):
        self.name = input("Введите имя компьютера:\t")
        self.motherboard = None
        self.isWork = False

    def insert_motherboard(self, mama):
        self.motherboard = mama
        print("Материнская плата установлена в компьютер!")

    def turn_on_pc(self):
        if self.motherboard is None:
            print("Нет материнской платы, как ты хочешь включить ПК??")
        elif self.motherboard is not None:
            if (self.motherboard.gpu) and (self.motherboard.cpu) and (self.motherboard.ram) is not None:
                print(f"Компьютер включён\n"
                      f"\tДобро пожаловать: {self.name}")
                self.isWork = True
            else:
                print("Ой, чего-то не хватает)")

    def turn_off_pc(self):
        if self.isWork:
            print("Компьютер выключен")
        else:
            print("Компьютер итак выключён...")

    def disconnect_motherboard(self):
        if self.motherboard is None:
            print("Материнской платы нет в ПК")
        elif self.motherboard is not None:
            self.motherboard = None


print("Вас приветствует программа сборки ПК")
motherboards = []
while True:
    print("Выберите действие\n"
          "\t1 -\tСобрать материнскую плату\n"
          "\t2 -\tНачать работу с компьютером\n"
          "\t3 -\tВыйти из программы")
    user_choice = Convert.string_to_int()
    if user_choice == 1:
        _motherboard = MotherBoard()
        while True:
            print("Выберите действие для работы с мат. платой:\n"
                  "\t1 -\tВставить компонент\n"
                  "\t2 -\tУдалить компонент\n"
                  "\t3 -\tВывести информацию о плате\n"
                  "\t4 -\tНе работать с мат. платой")
            user_choice = Convert.string_to_int()
            if 1 <= user_choice <= 4:
                if user_choice == 1:
                    _motherboard.insert_component()
                elif user_choice == 2:
                    _motherboard.del_component()
                elif user_choice == 3:
                    _motherboard.info_motherboard()
                elif user_choice == 4:
                    motherboards.append(_motherboard)
                    break
            else:
                print("Такого выбора нет")
    elif user_choice == 2:
        myComputer = PersonalComputer()
        while True:
            print("Выберите действие для работы с компьютером:\n"
                  "\t1 -\tВставить мат. плату\n"
                  "\t2 -\tОтключить мат. плату\n"
                  "\t3 -\tВключить компьютер\n"
                  "\t4 -\tВыключить компьютер\n"
                  "\t5 -\tНе работать с компьютером")
            user_choice = Convert.string_to_int()
            if 1 <= user_choice <= 5:
                if user_choice == 1:
                    print("Какую материнскую плату нужно вставить?")
                    j = 0
                    for i in motherboards:
                        j += 1
                        print(f"{j} - {i.name}")
                    motherboardinput = Convert.string_to_int() - 1
                    if motherboardinput < len(motherboards):
                        myComputer.insert_motherboard(motherboards[motherboardinput])
                    else:
                        print("Такой материнской платы нет!")
                elif user_choice == 2:
                    print("Материнская плата отключена")
                    myComputer.disconnect_motherboard()
                elif user_choice == 3:
                    myComputer.turn_on_pc()
                elif user_choice == 4:
                    myComputer.turn_off_pc()
                elif user_choice == 5:
                    break
            else:
                print("Такой функции нет!")
    elif user_choice == 3:
        break
