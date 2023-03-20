import sys, time
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsObject, QRadioButton, QFrame, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QPainterPath
from PyQt5.QtCore import Qt, QTime, QRectF, pyqtProperty, QEasingCurve, QTimer

class Teapot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(10)
        self.start_time = QTime.currentTime()

    def initUI(self):
         self.setWindowTitle("Лабораторная 7 Медведев Андрей ПКС-320")
         self.setGeometry(100, 100, 800, 800)
         self.show()

    def paintEvent(self, e):
        self.brush = QBrush(Qt.SolidPattern)
        self.brush.setColor(Qt.white)
        qp = QPainter()
        qp.begin(self)
        elapsed_time = self.start_time.elapsed()
        if elapsed_time % 500 < 250:
            self.draw_teapot(qp)
        else:
            self.draw_teapot_another(qp)
        qp.end()

    def draw_teapot(self, qp):
        pen = QPen(Qt.black)
        pen.setWidth(3)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(Qt.white)

        qp.setBrush(brush)
        qp.setPen(pen)
        # Ручка чайника
        path = QPainterPath()
        brush.setColor(Qt.red)
        qp.setBrush(brush)
        qp.setPen(pen)
        path.moveTo(110, 270)
        path.cubicTo(50, 200, -150, 400, 300, 400)
        path.cubicTo(50, 200, -110, 400, 300, 350)
        qp.drawPath(path)


        # Носик чайника
        path = QPainterPath()
        brush.setColor(Qt.darkBlue)
        qp.setBrush(brush)
        qp.setPen(pen)
        path.moveTo(410, 300)
        path.cubicTo(700, 200, 250, 400, 350, 360)
        path.lineTo(330, 320)
        path.closeSubpath()
        qp.drawPath(path)


        # Крышка носика
        brush.setColor(Qt.white)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(493, 268, 17, 17)

        # Подставка чайника
        brush.setColor(Qt.gray)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(150, 430, 200, 35)

        # Тело чайника
        brush.setColor(Qt.yellow)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(100, 150, 300, 300)

        # Крышка чайника
        brush.setColor(Qt.darkGreen)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(150, 100, 200, 200)

        # Пипка на крышке
        brush.setColor(Qt.gray)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(225, 80, 50, 50)

    def draw_teapot_another(self, qp):
        pen = QPen(Qt.black)
        pen.setWidth(3)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(Qt.white)

        qp.setBrush(brush)
        qp.setPen(pen)
        # Ручка чайника
        path = QPainterPath()
        brush.setColor(Qt.red)
        qp.setBrush(brush)
        qp.setPen(pen)
        path.moveTo(110, 270)
        path.cubicTo(50, 200, -150, 400, 300, 400)
        path.cubicTo(50, 200, -110, 400, 300, 350)
        qp.drawPath(path)

        # Носик чайника
        path = QPainterPath()
        brush.setColor(Qt.darkBlue)
        qp.setBrush(brush)
        qp.setPen(pen)
        path.moveTo(410, 300)
        path.cubicTo(700, 200, 250, 400, 350, 360)
        path.lineTo(330, 320)
        path.closeSubpath()
        qp.drawPath(path)

        # Крышка носика
        brush.setColor(Qt.white)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(493, 260, 17, 17)

        # Пар
        pen.setColor(Qt.yellow)
        qp.drawLine(500, 230, 493, 170)
        qp.drawLine(520, 230, 560, 170)
        qp.drawLine(483, 210, 470, 170)



        # Подставка чайника
        brush.setColor(Qt.gray)
        pen.setColor(Qt.black)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(150, 430, 200, 35)

        # Тело чайника
        brush.setColor(Qt.yellow)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(100, 150, 300, 300)

        # Крышка чайника
        brush.setColor(Qt.darkGreen)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(150, 50, 200, 200)

        # Пипка на крышке
        brush.setColor(Qt.gray)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawEllipse(225, 30, 50, 50)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    teapot = Teapot()
    sys.exit(app.exec_())
