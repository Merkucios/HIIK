from PyQt5 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        print(f"Поток запущен? {QtCore.QThread.isRunning(self)}")

    def run(self):
        while True:
            print(f"Поток запущен? {QtCore.QThread.isRunning(self)}")
            print(f"Приоритет потока = {QtCore.QThread.priority(self)} ")
            s = int(input("Измените поток\t"))
            if s == -1:
                print("Поток принудительно завершён")
                return -1
            else:
                self.setPriority(s)
                print(f"Приоритет потока = {QtCore.QThread.priority(self)} ")


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Нажмите кнопку для запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton("Запустить процесс")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.MyThread = MyThread()
        self.button.clicked.connect(self.on_clicked)
        self.MyThread.started.connect(self.on_started)
        self.MyThread.finished.connect(self.on_finished)
        self.MyThread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)
        self.MyThread.start()

    def on_started(self):
        self.label.setText("Вызван метод on_started()")

    def on_finished(self):
        self.label.setText("Вызван метод on_finished()")
        self.button.setDisabled(False)

    def on_change(self):
        self.label.setText(s)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
