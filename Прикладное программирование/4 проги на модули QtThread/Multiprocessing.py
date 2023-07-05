import math
import os
from multiprocessing import Process


def doubler(number):
    # Квадратный корень числа
    result = math.sqrt(number)
    proc = os.getpid()
    print(f"Квадратный корень числа {number} = {result}.\n\tID процесса: {proc}")


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    input("Чтобы завершить программу введите что-нибудь")