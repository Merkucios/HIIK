import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from MainForm import *
from PyQt5.QtWinExtras import QtWin


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer(self)
        self.setMouseTracking(True)
        self.changeColor = True

    def mouseMoveEvent(self, event):
        if event.MouseMove and self.changeColor:
            x = event.localPos().x()
            y = event.localPos().y()
            r = int(x / self.width() * 255)
            g = int(y / self.height() * 255)
            b = 150
            color = QtGui.QColor(r,g,b)
            palette = self.palette()
            palette.setColor(QtGui.QPalette.Window, color)
            self.setPalette(palette)


    def keyPressEvent(self, event):
        if event.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.AltModifier) and event.key() == QtCore.Qt.Key_Q:
            self.changeColor = not self.changeColor
        elif event.key() == QtCore.Qt.Key_Up:
            self.move(self.x(), self.y() - 10)
        elif event.key() == QtCore.Qt.Key_Down:
            self.move(self.x(), self.y() + 10)
        elif event.key() == QtCore.Qt.Key_Left:
            self.move(self.x() - 10, self.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.move(self.x() + 10, self.y())
        elif event.key() == QtCore.Qt.Key_F5:
            self.close()
        if event.modifiers() == QtCore.Qt.AltModifier and event.key() == QtCore.Qt.Key_X:
            self.close()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if event.modifiers() == QtCore.Qt.AltModifier:
                self.resize(self.width() + 5, self.height() + 5)
            elif event.modifiers() == QtCore.Qt.ShiftModifier:
                self.resize(self.width() - 5, self.height() - 5)
        elif event.button() == QtCore.Qt.MiddleButton:
            self.move_center()



    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton and not event.modifiers():
            self.close()

    def move_center(self):
        desktop = QtWidgets.QDesktopWidget()
        screen = desktop.screenGeometry(desktop.primaryScreen())
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Закрыть форму', 'Вы уверены, что хотите закрыть форму?',
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myappid = 'my_version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QtGui.QIcon("iconic.jpg"))
    window = GUI()
    window.show()
    sys.exit(app.exec_())




