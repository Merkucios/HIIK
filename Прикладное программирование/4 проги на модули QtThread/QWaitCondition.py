from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("QCondition")
        Dialog.resize(275, 126)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 211, 85))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Проверка QWaitCondition"))
        self.label.setText(_translate("Dialog", "Сумма:"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.pushButton_2.setText(_translate("Dialog", "Пауза"))
        self.pushButton_3.setText(_translate("Dialog", "Продолжить"))


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self._isPause = False
        self.condition = QWaitCondition()
        self.mutex = QMutex()
        self.sum = 0

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.condition.wakeAll()

    def run(self):
        while True:
            self.mutex.lock()
            if self._isPause:
                self.condition.wait(self.mutex)
            self.sum += 1
            time.sleep(2)
            self.mutex.unlock()

class Window(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threads = []
        self.sum = 0
        self.count = 1
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(6000)

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_3.clicked.connect(self.resume)

    def update(self):
        self.sum = 0
        for i in range(len(self.threads)):
            self.sum += self.threads[i].sum
        self.label_2.setText(str(self.sum))

    def add(self):
        self.thread = Thread()
        self.comboBox.addItem(f'Поток #{self.count}')
        self.thread.start()
        self.threads.append(self.thread)
        self.count += 1

    def stop(self):
        id = self.comboBox.currentIndex()
        self.threads[id].pause()

    def resume(self):
        id = self.comboBox.currentIndex()
        self.threads[id].resume()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())