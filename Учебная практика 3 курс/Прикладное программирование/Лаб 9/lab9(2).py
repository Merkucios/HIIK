import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QAction, QTextEdit, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont

class IntermediateValues(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)

        # Создание текстового поля для вывода промежуточных значений
        self.textEdit = QTextEdit()
        self.setWindowTitle('Промежуточные значения') # Установка заголовка окна
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFont(QFont("Times New Roman", 12))
        self.textEdit.setReadOnly(True)

    # Функция для вывода промежуточных значений в текстовое поле
    def print_intermediate_value(self, value):
        self.textEdit.append(str(value))



class ArrayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная 9 Медведев Андрей")
        self.resize(300, 200)
        self.array = ''
        self.intermed = IntermediateValues()
        # Создание элементов управления
        self.dim_label = QLabel("Многомерность массива:")
        self.dim_combo = QComboBox()
        self.dim_combo.addItems(["Одномерный", "Двумерный"])

        self.array_size_label = QLabel("Размер массива:")
        self.array_size_edit = QLineEdit()
        self.array_size_edit.setPlaceholderText("Введите размер массива")

        self.subarray1_label = QLabel("Размер первого подмассива:")
        self.subarray1_edit = QLineEdit()
        self.subarray1_edit.setPlaceholderText("Введите размер первого подмассива")

        self.subarray2_label = QLabel("Размер второго подмассива:")
        self.subarray2_edit = QLineEdit()
        self.subarray2_edit.setPlaceholderText("Введите размер второго подмассива")

        self.sort_label = QLabel("Сортировка массива:")
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["По убыванию", "По возрастанию"])

        self.generate_button = QPushButton("Сгенерировать массив")
        self.sort_button = QPushButton("Сортировать")
        self.intermediate_values = QPushButton("Задание 1")
        self.intermediate_values_2 = QPushButton("Задание 2")

        self.result_label = QLabel()

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
        self.intermediate_values.clicked.connect(self.find_row_with_max_in_column)
        self.intermediate_values_2.clicked.connect(self.find_cols_with_min_in_row)

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
        if self.dim_combo.currentIndex() == 0:  # Одномерный массив
            size = int(self.array_size_edit.text())
            self.array = np.random.randint(1, 20, size=size)
        elif self.dim_combo.currentIndex() == 1:  # Двумерный массив
            size1 = int(self.subarray1_edit.text())
            size2 = int(self.subarray2_edit.text())
            self.array = np.random.randint(1, 20, size=(size1, size2))
        else:
            return  # Ничего не делать, если не выбран тип массива
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

    def find_row_with_max_in_column(self):
        try:
            num_rows = len(self.array)
            num_cols = len(self.array[0])
        except IndexError:
            msg = QMessageBox.information(self, "Массив", "Сгенерируйте массив")
            return
        except TypeError:
            msg = QMessageBox.information(self, "Массив", "Только для двухмерных массивов")
            return
        index_max_colum = []

        for j in range(num_cols):
            self.intermed.print_intermediate_value(f"* Начинаю поиск в столбце {j + 1}:")
            max_val = self.array[0][j]
            max_row = 0
            for i in range(num_rows):
                self.intermed.print_intermediate_value(f"** Смотрю строку {i + 1} со значением {self.array[i][j]}")
                self.intermed.print_intermediate_value(f"*** {self.array[i][j]} > {max_val} ?")
                if self.array[i][j] > max_val:
                    max_val = self.array[i][j]
                    max_row = i
                if i == num_rows - 1:
                    index_max_colum.append(max_row + 1)
                self.intermed.print_intermediate_value(f"**** Максимальное значение в колонке {j + 1} это {max_val} в строке {max_row + 1}\n")
            self.intermed.print_intermediate_value(f"***** Список с индексами строк макс.элементов в столбце {index_max_colum}\n")
            self.intermed.show()

    def find_cols_with_min_in_row(self):
        try:
            num_rows = len(self.array)
            num_cols = len(self.array[0])
        except IndexError:
            msg = QMessageBox.information(self, "Массив", "Сгенерируйте массив")
            return
        except TypeError:
            msg = QMessageBox.information(self, "Массив", "Только двухмерные массивы")
            return
        index_min_rows = []

        for i in range(num_rows):
            self.intermed.print_intermediate_value(f"* Начинаю поиск в строке {i + 1}:")
            min_val = self.array[i][0]
            min_col = 0
            for j in range(num_cols):
                self.intermed.print_intermediate_value(f"** Смотрю столбец {j + 1} со значением {self.array[i][j]}")
                self.intermed.print_intermediate_value(f"*** {self.array[i][j]} < {min_val} ?")
                if self.array[i][j] < min_val:
                    min_val = self.array[i][j]
                    min_col = i
                if j == num_cols - 1:
                    index_min_rows.append(min_col + 1)
                self.intermed.print_intermediate_value(f"**** Минимальное значение в строке {j + 1} это {min_val} в столбце {min_col + 1}\n")
            self.intermed.print_intermediate_value(f"***** Список с индексами столбцов мин.элементов в строке {index_min_rows}\n")
            self.intermed.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    array_app = ArrayApp()
    array_app.run()
    sys.exit(app.exec_())