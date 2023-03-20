def firstTask(num):
    # 9 = 3 - true
    # 2 - false
    for i in range(1, num):
        if i ** 2 == num:
            print(f"Число {i} квадрат числа {num}")
            return True
        elif i is num - 1:
            print(f"Нет квадрата числа {num}")
            return False
def secondTask():
    def invert_word(word):
        if len(word) > 5:
            return word[0] + word[-2:0:-1] + word[-1]
        else:
            return word

    text = input("Введите строку без знаков препинаний:\t")
    splittedString = text.split(" ")
    result = list(map(invert_word, splittedString))
    return ' '.join(result)


def thirdTask(myList):
    indexOfZero = 0

    for i in range(len(myList)):
        if myList[i] != 0:
            myList[i], myList[indexOfZero] = myList[indexOfZero], myList[i]
            indexOfZero += 1
    return myList



print("Тест 3 задачи")
listJ = [1, 3, 990, 2, 4, 0, 13, 4, 0, 2]
print(listJ)
print(thirdTask(listJ))
