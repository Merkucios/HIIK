import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Функции рекурсии')
        self.setGeometry(200, 200, 400, 300)

        self.label_a = QLabel('Введите число a:', self)
        self.label_a.move(10, 10)
        self.edit_a = QLineEdit(self)
        self.edit_a.move(120, 10)

        self.label_b = QLabel('Введите число b:', self)
        self.label_b.move(10, 40)
        self.edit_b = QLineEdit(self)
        self.edit_b.move(120, 40)

        self.label_result = QLabel('Результат:', self)
        self.label_result.move(10, 130)
        self.result = QLabel('', self)
        self.result.move(120, 130)
        self.result.resize(120,130)

        self.button_gcd = QPushButton('НОД', self)
        self.button_gcd.move(10, 80)
        self.button_gcd.clicked.connect(self.find_gcd)

        self.button_ackermann = QPushButton('Аккерман', self)
        self.button_ackermann.move(100, 80)
        self.button_ackermann.clicked.connect(self.ackermann)

        self.button_digit_sum = QPushButton('Сумма цифр', self)
        self.button_digit_sum.move(190, 80)
        self.button_digit_sum.clicked.connect(self.digit_sum)

        self.button_clear = QPushButton('Очистить', self)
        self.button_clear.move(280, 80)
        self.button_clear.clicked.connect(self.clear_fields)

        self.show()

    def find_gcd(self):
        a = int(self.edit_a.text())
        b = int(self.edit_b.text())
        gcd = gcd_recursive(a, b)
        self.result.setText(str(gcd))

    def ackermann(self):
        m = int(self.edit_a.text())
        n = int(self.edit_b.text())
        if m >= 4 or n >= 4:
            msgBox = QMessageBox.information(self, "Тяжело", "  К сожалению функция Аккермана быстро растёт\n  И из-за этого Питон\n  Вылетает!!!!")
        else:
            ack = ackermann_recursive(m, n)
            self.result.setText(str(ack))

    def digit_sum(self):
        n = abs(int(self.edit_a.text()))
        m = abs(int(self.edit_b.text()))
        sum_digits = digit_sum_recursive(n)
        sum_digits += digit_sum_recursive(m)
        self.result.setText(str(sum_digits))

    def clear_fields(self):
        self.edit_a.clear()
        self.edit_b.clear()
        self.result.setText('')


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def ackermann_recursive(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_recursive(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann_recursive(m - 1, ackermann_recursive(m, n - 1))



def digit_sum_recursive(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + digit_sum_recursive(n // 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
