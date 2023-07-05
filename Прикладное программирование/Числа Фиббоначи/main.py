from des import *
from PyQt5 import QtCore, QtWidgets
import sys
import time


def fib_recursia(n):
    if n in [1, 2]:
        return 1
    return fib_recursia(n - 1) + fib_recursia(n - 2)


def fib_chislo(n):
    fib1 = fib2 = 1

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2


class FirstThread(QtCore.QThread):
    def __init__(self, changewindow=None):
        super().__init__()
        self.changewindow = changewindow
        self.number = 0

    def run(self):
        self.number = int(self.changewindow.lineEdit.text())
        now = time.time()
        fib = fib_recursia(self.number)
        self.changewindow.first_value.setText(str(fib))
        self.changewindow.first_time.setText(str(time.time() - now))


class SecondThread(QtCore.QThread):
    def __init__(self, changewindow=None):
        super().__init__()
        self.changewindow = changewindow
        self.number = 0

    def run(self):
        self.number = int(self.changewindow.lineEdit.text())
        print('Поток #2 - 1')
        now = time.time()
        self.number = fib_chislo(self.number)
        print('Поток #2 - 2')
        self.changewindow.second_value.setText(str(self.number))
        self.changewindow.second_time.setText(str(time.time() - now))


class Ui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        self.firstthread = FirstThread(self.ui)
        self.secondthread = SecondThread(self.ui)
        self.firstthread.start()
        self.secondthread.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
