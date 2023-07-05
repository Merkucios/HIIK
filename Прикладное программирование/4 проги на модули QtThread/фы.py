from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QThread
import time
import msvcrt
import random


def wait():
    i = int(input())
    return i


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self._isPause = False
        self.opaqueness = 0
        self.count = 0
        self.start()

    def check(self):
        self.opaqueness += 0.1
        splash.setWindowOpacity(self.opaqueness)
        if self.opaqueness > 0.9:
            print('Завершено')
            app.exit()

    def run(self):
        while True and self.count < 10:
            x = random.randint(1, 5)
            y = random.randint(1, 6)
            print("(" + str(self.count) + "0%)", x, "+", y, "=")
            z = wait()
            if (z == (x + y)):
                print('Верно')
                self.count += 1
                self.check()
            else:
                print('Неверно')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    splash_pix = QtGui.QPixmap('picture.jpg')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setWindowOpacity(0)
    splash.show()
    th = Thread()
    app.exec_()