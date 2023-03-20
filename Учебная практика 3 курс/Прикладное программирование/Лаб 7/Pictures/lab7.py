import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class StringManipulator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        input_label = QLabel('Введите строку:')
        self.input_field = QLineEdit()

        output_label = QLabel('Вывод:')
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)

        self.result_button = QPushButton('Вывести результат')
        self.result_button.clicked.connect(self.show_result)

        self.clear_button = QPushButton('Очистить форму')
        self.clear_button.clicked.connect(self.clear_form)

        hbox = QHBoxLayout()
        hbox.addWidget(self.result_button)
        hbox.addWidget(self.clear_button)

        vbox = QVBoxLayout()
        vbox.addWidget(input_label)
        vbox.addWidget(self.input_field)
        vbox.addWidget(output_label)
        vbox.addWidget(self.output_field)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('String Manipulator')
        self.show()

    def show_result(self):
        input_str = self.input_field.text()
        output_str = ""        if len(input_str) == 1:
            QMessageBox.information(self, 'Внимание!', 'Дальше удалять нельзя!')
            return        for i in range(len(input_str)):
            output_str += input_str[:len(input_str) - i] + "\n"        output_str += 'Больше удалять нельзя!\n'        for i in range(len(input_str) - 1, -1, -1):
            output_str += input_str[i:len(input_str) + 1] + "\n"        self.output_field.setText(output_str)

    def clear_form(self):
        self.input_field.setText("")
        self.output_field.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StringManipulator()
    sys.exit(app.exec_())