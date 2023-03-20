import sys, random
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QAction, QTextEdit, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class IntermediateValues(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)

        # Создание текстового поля для вывода промежуточных значений
        self.textEdit = QTextEdit()
        self.setWindowTitle('Промежуточные значения') # Установка заголовка окна
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFont(QFont("Calibri", 12))
        self.textEdit.setReadOnly(True)

    # Функция для вывода промежуточных значений в текстовое поле
    def print_intermediate_value(self, value):
        self.textEdit.append(str(value))



class ArrayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная 9 Медведев Андрей")
        self.resize(500, 500)
        self.array = ''
        self.intermed = IntermediateValues()
        self.intermed_2 = IntermediateValues()

        self.setFont(QFont("Century", 10))

        self.dim_label = QLabel("Многомерность массива:")
        self.dim_combo = QComboBox()
        self.dim_combo.addItems(["Одномерный", "Двумерный"])

        self.array_size_label = QLabel("Размер массива:")
        self.array_size_edit = QLineEdit()
        self.array_size_edit.setPlaceholderText("Введите размер массива")

        self.subarray1_label = QLabel("Количество строк:")
        self.subarray1_edit = QLineEdit()
        self.subarray1_edit.setPlaceholderText("Введите количество строк массива")

        self.subarray2_label = QLabel("Количество столбцов:")
        self.subarray2_edit = QLineEdit()
        self.subarray2_edit.setPlaceholderText("Введите количество столбцов массива")

        self.sort_label = QLabel("Сортировка массива:")
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["По убыванию", "По возрастанию"])

        self.generate_button = QPushButton("Сгенерировать массив")
        self.sort_button = QPushButton("Сортировать")
        self.intermediate_values = QPushButton("Задание 1")
        self.intermediate_values_2 = QPushButton("Задание 2")

        self.result_label = QTextEdit()
        self.result_label.setReadOnly(True)
        self.result_label.resize(400, 300)

        # Создание компоновщика
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.dim_label)
        self.layout.addWidget(self.dim_combo)
        self.layout.addWidget(self.array_size_label)
        self.layout.addWidget(self.array_size_edit)
        self.layout.addWidget(self.subarray1_label)
        self.layout.addWidget(self.subarray1_edit)
        self.layout.addWidget(self.subarray2_label)
        self.layout.addWidget(self.subarray2_edit)
        self.layout.addWidget(self.sort_label)
        self.layout.addWidget(self.sort_combo)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.sort_button)
        self.layout.addWidget(self.intermediate_values)
        self.layout.addWidget(self.intermediate_values_2)
        self.layout.addWidget(self.result_label)

        # Установка компоновщика
        self.setLayout(self.layout)

        # Подключение обработчиков событий
        self.dim_combo.currentIndexChanged.connect(self.on_dim_changed)
        self.generate_button.clicked.connect(self.generate_array)
        self.sort_button.clicked.connect(self.sort_array)
        self.intermediate_values.clicked.connect(self.task_a)
        self.intermediate_values_2.clicked.connect(self.task_b)

        self.subarray1_label.hide()
        self.subarray1_edit.hide()
        self.subarray2_label.hide()
        self.subarray2_edit.hide()

    def on_dim_changed(self, index):
        # Показать/скрыть элементы управления в зависимости от выбранной многомерности
        if index == 0:
            self.array_size_label.show()
            self.array_size_edit.show()
            self.subarray1_label.hide()
            self.subarray1_edit.hide()
            self.subarray2_label.hide()
            self.subarray2_edit.hide()
        elif index == 1:
            self.array_size_label.hide()
            self.array_size_edit.hide()
            self.subarray1_label.show()
            self.subarray1_edit.show()
            self.subarray2_label.show()
            self.subarray2_edit.show()


    def generate_array(self):
        if self.dim_combo.currentIndex() == 0:
            size = int(self.array_size_edit.text())
            self.array = np.random.randint(1, 15, size=size)
        elif self.dim_combo.currentIndex() == 1:
            size1 = int(self.subarray1_edit.text())
            size2 = int(self.subarray2_edit.text())
            self.array = np.random.randint(1, 15, size=(size1, size2))
        else:
            return
        self.result_label.setText(str(self.array))


    def sort_array(self):
        if self.sort_combo.currentIndex() == 0:
            self.array = np.sort(self.array)[::-1]
        elif self.sort_combo.currentIndex() == 1:
            self.array = np.sort(self.array)
        self.result_label.setText(str(self.array))

    def run(self):
        self.show()
        sys.exit(app.exec_())

    def task_a(self):
        self.intermed.print_intermediate_value(f"Массив:")
        for row in self.array:
            self.intermed.print_intermediate_value(row)
        try:
            num_rows = len(self.array)
            num_cols = len(self.array[0])
        except (ValueError, IndexError):
            msg = QMessageBox.information(self, "Ошибка", "Сгенерируйте массив")
            return

        k = random.randint(0, num_cols - 1)
        self.intermed.print_intermediate_value(("K = {}".format(k)))
        product = 1
        for i in range(num_rows):
            elem = self.array[i][k]
            product *= elem
            self.intermed.print_intermediate_value(f"{product} * {elem}")
            self.intermed.print_intermediate_value("Промежуточный результат: {}".format(product))
        checkProduct = product
        k = 0
        while checkProduct >= 1:
            k += 1
            checkProduct //= 10
        if k == 3:
            self.intermed.print_intermediate_value("Произведение элементов в столбце {} это трёхзначное число".format(k))
        else:
            self.intermed.print_intermediate_value("Произведение элементов в столбце {} это НЕтрёхзначное число".format(k))
        self.intermed.show()

    def task_b(self):
        try:
            num_rows = len(self.array)
            num_cols = len(self.array[0])
        except (ValueError, IndexError):
            msg = QMessageBox.information(self, "Ошибка", "Сгенерируйте массив")
            return
        self.intermed_2.print_intermediate_value(f"Массив:")
        for row in self.array:
            self.intermed_2.print_intermediate_value(row)
        i = random.randint(0, num_rows - 1)
        self.intermed_2.print_intermediate_value(f"Строка: {i + 1}")
        s = random.randint(10, 75)
        self.intermed_2.print_intermediate_value(f"Число: {s}")
        row = self.array[i]
        sum = 0
        for elem in row:
            self.intermed_2.print_intermediate_value(f"{sum} + {elem} = {sum + elem}")
            sum += elem
        self.intermed_2.print_intermediate_value(f"{sum} > {s}?")
        if sum > s:
            self.intermed_2.print_intermediate_value("Сумма элементов в строки {} превышает число {}".format(i + 1, s))
        else:
            self.intermed_2.print_intermediate_value("Сумма элементов строки {} не превышает число {}".format(i + 1, s))
        self.intermed_2.move(200, 200)
        self.intermed_2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    array_app = ArrayApp()
    array_app.run()
    sys.exit(app.exec_())