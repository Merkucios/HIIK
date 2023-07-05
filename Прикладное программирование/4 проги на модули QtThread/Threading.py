import threading

threadId = 1
thread1 = threading.Thread()
thread2 = threading.Thread()


def factorial(n):
    global threadId
    if n < 1:
        print(f"Thread {threadId}")
        threadId += 1
        return 1
    else:
        returnNumber = n * factorial(n - 1)
        print(f"{n} != {returnNumber}")
        return returnNumber


try:
    thread1.start(factorial(13))
except (ValueError, TypeError) as err:
    pass

try:
    thread2.start(factorial(3))
except (ValueError, TypeError) as err:
    pass

c = input("Завершите программу....\n")
