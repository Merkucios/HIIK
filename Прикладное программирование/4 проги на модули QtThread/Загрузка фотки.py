import random

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Закрыть окно")
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self, sp):
        task = [2, 2, 6, 27, 6, 2, 15, 64, 3, 8]
        exp = ["1+1", "3-1", "4+2", "3*9", "3!", "ln(100)", "11+2*2", "8^2", "13-10", "9-1"]
        sp.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        for i in range(10):
            print(f"Решите уравнение\t{exp[i]}")
            while True:
                try:
                    k = int(input("Введите решение уравнения\t"))
                except ValueError as err:
                    print("Введите число!")
                else:
                    break

            if k == task[i]:
                sp.showMessage("Загрузка данных... {0}%".format(i * 10),
                               QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)
                QtWidgets.qApp.processEvents()

    def select_picture(self):
        jpg = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
        loj = random.randint(1,4)
        return QtWidgets.QSplashScreen(QtGui.QPixmap(f"{loj}.jpg"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(f"8.jpg"))
    splash.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
    splash.showMessage("Загрузка данных... 0%",
                       QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)
    splash.show()
    QtWidgets.qApp.processEvents()
    window = MyWindow()
    window.setWindowTitle("Решение задачек")
    window.resize(300, 30)
    window.load_data(splash)
    window.select_picture()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
