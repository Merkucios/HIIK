from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
import sys
from PyQt5 import QtWidgets

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Лабораторная работа №6 Медведев Андрей")
        self.resize(600,600)
        # Создание компонентов
        self.input_label = QLabel('Введите слово:')
        self.input_edit = QLineEdit()
        self.n_label = QLabel('Введите номера букв для удаления через запятую:')
        self.n_edit = QLineEdit()
        self.output_label = QLabel('Результат:')
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)
        self.result_button = QPushButton('Результат')
        self.result_button.clicked.connect(self.show_result)
        self.clear_button = QPushButton('Очистить форму')
        self.clear_button.clicked.connect(self.clear_form)

        # Создание компоновщиков
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_edit)
        n_layout = QHBoxLayout()
        n_layout.addWidget(self.n_label)
        n_layout.addWidget(self.n_edit)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.result_button)
        button_layout.addWidget(self.clear_button)
        output_layout = QVBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_edit)
        output_layout.addLayout(button_layout)
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(n_layout)
        main_layout.addLayout(output_layout)
        self.setLayout(main_layout)

    def show_result(self):
        # Получение входных данных
        word = self.input_edit.text()
        try:
            letters_to_remove = self.n_edit.text().split(',')  # Получение номеров букв для вычеркивания
            letters_to_remove = [int(x.strip()) for x in letters_to_remove]  # Преобразование номеров букв в целочисленный формат
            letters_to_remove.sort(reverse=True)
        except ValueError:
            msgBox = QtWidgets.QMessageBox.critical(self, "Ошибка!", "Введите номера букв!")
            return

        # Проверка на вычеркивание всех букв
        if 1 in letters_to_remove:
            msgBox = QtWidgets.QMessageBox.information(self, "Буквы", "Все буквы вычеркнуты!")
            return

        # Вычеркивание каждой n-ой буквы
        for i in letters_to_remove:
            word = word[:i - 1] + word[i:]

        # Вывод результата
        self.output_edit.setText(word)

    def clear_form(self):
        # Очистка всех компонентов
        self.input_edit.setText('')
        self.n_edit.setText('')
        self.output_edit.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
