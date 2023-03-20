import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit


class NumberComparison(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сравнение суммы цифр двух чисел')
        self.setGeometry(100, 100, 400, 200)

        # create line edits
        self.num1_edit = QLineEdit(self)
        self.num2_edit = QLineEdit(self)

        # create labels
        self.label1 = QLabel('Первое число:', self)
        self.label2 = QLabel('Второе число:', self)
        self.result_label = QLabel('', self)
        self.resultSum_label = QLabel('', self)
        self.resultSum2_label = QLabel('', self)

        # create buttons
        self.compare_button = QPushButton('Сравнить числа', self)
        self.compare_button.clicked.connect(self.compare_numbers)

        self.random_button = QPushButton('Случайные числа', self)
        self.random_button.clicked.connect(self.generate_numbers)

        self.clear_button = QPushButton('Очистить форму', self)
        self.clear_button.clicked.connect(self.clear_form)

        # create layouts
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.label2)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.num1_edit)
        vbox2.addWidget(self.num2_edit)

        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.result_label)
        vbox3.addStretch(1)

        vbox4 = QVBoxLayout()
        vbox4.addWidget(self.resultSum_label)
        vbox4.addStretch(1)

        vbox5 = QVBoxLayout()
        vbox5.addWidget(self.resultSum2_label)
        vbox5.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.compare_button)
        hbox2.addWidget(self.random_button)
        hbox2.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox1)
        main_layout.addLayout(vbox3)
        main_layout.addLayout(hbox2)
        main_layout.addLayout(vbox4)
        main_layout.addLayout(vbox5)

        self.setLayout(main_layout)

        self.show()

    def compare_numbers(self):
        try:
            num1 = int(self.num1_edit.text())
            num2 = int(self.num2_edit.text())
            sum1 = 0
            for digit in str(num1):
                sum1 += int(digit)
                self.resultSum_label.setText(f'Сумма цифр первого числа: {sum1}')

            sum2 = 0
            for digit in str(num2):
                sum2 += int(digit)
                self.resultSum2_label.setText(f'Сумма цифр второго числа: {sum2}')
            if sum1 > sum2:
                self.result_label.setText('Сумма цифр первого числа больше')
            elif sum2 > sum1:
                self.result_label.setText('Сумма цифр второго числа больше')
            else:
                self.result_label.setText('Сумма цифр двух чисел одинакова')
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Введите правильные значения!')

    def generate_numbers(self):
        num1 = str(random.randint(1, 9999))
        num2 = str(random.randint(1, 9999))
        self.num1_edit.setText(num1)
        self.num2_edit.setText(num2)
        self.result_label.setText('')

    def clear_form(self):
        self.num1_edit.setText('')
        self.num2_edit.setText('')
        self.result_label.setText('')
        self.resultSum_label.setText('')
        self.resultSum2_label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NumberComparison()
    sys.exit(app.exec_())
