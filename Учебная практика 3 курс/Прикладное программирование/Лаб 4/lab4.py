import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from FormFor4Lab import *

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.block = False
        self.WinEnabled = True

        self.ui.pushButton.clicked.connect(self.button1_click)
        self.ui.pushButton_2.clicked.connect(self.button2_click)
        self.ui.pushButton_3.clicked.connect(self.button3_click)
        self.ui.pushButton_4.clicked.connect(self.button4_click)

        self.ui.pushButton.setToolTip('Эта кнопка <b>переключает блокировку 2-й и 3-й</b>')
        self.ui.pushButton_2.setToolTip('Эта <u>кнопка</u> сдвигает первую кнопку на 10 пикселей вниз + увеличивает размер третей кнопки на 2 пикселя')
        self.ui.pushButton_3.setToolTip('Эта кнопка <i>меняет</i> стили шрифтов')
        self.ui.pushButton_4.setToolTip('Эта кнопка <b><i><u> отключает/включает Win-кнопки')

    def move_center(self):
        desktop = QtWidgets.QDesktopWidget()
        screen = desktop.screenGeometry(desktop.primaryScreen())
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_I and event.modifiers() == QtCore.Qt.AltModifier:
            self.move_center()
            self.restore_initial_state()
        if event.key() == QtCore.Qt.Key_X and event.modifiers() == QtCore.Qt.AltModifier:
            self.close()


    def restore_initial_state(self):
        self.resize(630, 400)
        self.ui.pushButton.setGeometry(QtCore.QRect(90, 50, 170, 70))
        self.ui.pushButton_2.setGeometry(QtCore.QRect(360, 50, 170, 70))
        self.ui.pushButton_3.setGeometry(QtCore.QRect(90, 200, 170, 70))
        self.ui.pushButton_4.setGeometry(QtCore.QRect(360, 200, 170, 70))

        self.ui.pushButton_2.setFont(QtGui.QFont())
        self.ui.pushButton_4.setFont(QtGui.QFont())

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Закрыть форму', 'Вы уверены, что хотите закрыть форму?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()





    def button1_click(self):
        self.block = not self.block
        isSecondButton = True
        if isSecondButton:
            self.ui.pushButton_2.setEnabled(self.block)
            self.ui.pushButton_3.setEnabled(not self.block)
            isSecondButton = False
        else:
            self.ui.pushButton_2.setEnabled(not self.block)
            self.ui.pushButton_3.setEnabled(self.block)

    def button2_click(self):
        if self.ui.pushButton.y() + self.ui.pushButton.height() + 30 < self.height():
            self.ui.pushButton.move(self.ui.pushButton.x(), self.ui.pushButton.y() + 10)
        if (self.ui.pushButton_3.x() + self.ui.pushButton_3.width() + 30 < self.width())\
                and (self.ui.pushButton_3.y() + self.ui.pushButton_3.height() + 30 < self.height()):
            self.ui.pushButton_3.resize(self.ui.pushButton_3.width() + 2, self.ui.pushButton_3.height() + 2)

    def button3_click(self):
        modifier = QtWidgets.QApplication.keyboardModifiers()
        fontButton2 = self.ui.pushButton_2.font()
        fontButton4 = self.ui.pushButton_4.font()

        if modifier == QtCore.Qt.ShiftModifier:
            fontButton2.setItalic(not fontButton2.italic())
            fontButton4.setItalic(not fontButton4.italic())
            self.ui.pushButton_2.setFont(fontButton2)
            self.ui.pushButton_4.setFont(fontButton4)
        elif modifier == QtCore.Qt.ControlModifier:
            fontButton2.setUnderline(not fontButton2.underline())
            fontButton4.setUnderline(not fontButton4.underline())
            self.ui.pushButton_2.setFont(fontButton2)
            self.ui.pushButton_4.setFont(fontButton4)
        else:
            fontButton2.setBold(not fontButton2.bold())
            fontButton4.setBold(not fontButton4.bold())
            self.ui.pushButton_2.setFont(fontButton2)
            self.ui.pushButton_4.setFont(fontButton4)

    def button4_click(self):
        def enableWindowsButtons(self):
                windowFlags = self.windowFlags()
                windowFlags |= QtCore.Qt.WindowCloseButtonHint
                windowFlags |= QtCore.Qt.WindowMinimizeButtonHint
                windowFlags |= QtCore.Qt.WindowMaximizeButtonHint
                self.setWindowFlags(windowFlags)
                self.show()

        def disableWindowsButtons(self):
                windowFlags = self.windowFlags()
                windowFlags &= ~QtCore.Qt.WindowCloseButtonHint
                windowFlags &= ~QtCore.Qt.WindowMinimizeButtonHint
                windowFlags &= ~QtCore.Qt.WindowMaximizeButtonHint
                self.setWindowFlags(windowFlags)
                self.show()

        if self.WinEnabled:
            disableWindowsButtons(self)
            self.WinEnabled = False
        else:
            enableWindowsButtons(self)
            self.WinEnabled = True






















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())