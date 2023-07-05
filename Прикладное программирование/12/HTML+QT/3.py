import sys
from PyQt5.QtWidgets import QApplication, QLabel, QScrollArea, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap


class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 600)
        self.setWindowTitle('Листание картинок с PyQt')
        self.img = QPixmap("glaz.jpg")
        scr = QScrollArea(self)
        pnl = QWidget(self)

        vbox = QVBoxLayout(self)
        for i in range(2):
            lbl = QLabel()
            lbl.setPixmap(self.img)
            vbox.addWidget(lbl)

        pnl.setLayout(vbox)
        scr.setWidget(pnl)
        self.setCentralWidget(scr)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())