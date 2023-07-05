# Метод объединяет данные по знаку пробела и с помощью map() преобразует список в строку
def JoinForSpace(some_list):
    return  " ".join(map(str,some_list))


# Метод разделяет строку на подстроки по знаку "," в зависимости от длины списка
def SplitForComma(some_list):
    return some_list.split(',', len(some_list))


# Метод реализующий ввод данных и приведение данных в список
def DataInputWithoutSpaceComma(user_list):
    user_list = []

    print("Введите несколько значений через запятую")

    unit_numbers = input()
    user_list.append(unit_numbers)

    quarter_result = JoinForSpace(user_list)

    for i in quarter_result:
        result_list = SplitForComma(quarter_result)
    return result_list


# Первое задание
def StringToIntNum(user_list):
    result_list = []
    result_list = DataInputWithoutSpaceComma(result_list)

    try:
        result_list = [int(i) for i in result_list]
    except ValueError:
        print("Вы ввели неправильное значние int")
        return []
    except NameError:
        print("Вы обратились к неправильной переменной")
        return []
    else:
        print(f"Полученный список: {result_list}")
        return result_list


# Второе задание
def AverageNumList(listnum):
    sum = 0

    for i in listnum:
        sum += i
    try:
        result = sum / len(listnum)
    except ZeroDivisionError:
        print(f"Ошибка деления на ноль. Список является пустым. {len(listnum)}")
    else:
        print(f"Полученное среднее арифметическое значение: {result}")


# Третье задание
def SetDeleteElement(elem_for_del):
    _set_input = []
    _set_input = DataInputWithoutSpaceComma(_set_input)
    del_elem = _set_input[elem_for_del]

    try:
        _set_input.pop(elem_for_del)
    except IndexError:
        print("Индекс превышает значение длины списка")
    except NameError:
        print("Вы обратились к неправильной переменной")
    else:
        _set_input = set(_set_input)
        return print(f"Полученное множество равно = {_set_input} ,удалённый элемент это - {del_elem} , типа {type(_set_input)}")


arr = []

print("*" * 5 + "Первое задание" + "*" * 5)
arr = StringToIntNum(arr)
print("*" * 5 + "Второе задание" + "*" * 5)
AverageNumList(arr)

user_elem_for_del = int(input("Введите индекс удаления из списка "))
print()

SetDeleteElement(user_elem_for_del)