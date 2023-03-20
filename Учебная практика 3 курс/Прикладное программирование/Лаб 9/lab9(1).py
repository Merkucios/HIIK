import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QTableWidget, \
    QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import random


class ArrayProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная работа №9 Медведев Андрей")
        self.setGeometry(100, 100, 1000, 1000)


        font = QFont()
        font.setPointSize(12)


        self.array_type_label = QLabel("Тип массива:", self)
        self.array_type_label.move(20, 20)
        self.array_type_label.setFont(font)

        self.array_type_combo = QComboBox(self)
        self.array_type_combo.addItems(["Одномерный"])
        self.array_type_combo.move(150, 20)
        self.array_type_combo.setFont(font)
        self.array_type_combo.currentIndexChanged.connect(self.update_array_type)


        self.array_dim_label = QLabel("Количество элементов:", self)
        self.array_dim_label.move(20, 60)
        self.array_dim_label.setFont(font)

        self.array_dim_edit = QLineEdit(self)
        self.array_dim_edit.move(250, 60)
        self.array_dim_edit.setFont(font)


        self.k_value_label = QLabel("Введите значение K:", self)
        self.k_value_label.move(20, 100)
        self.k_value_label.setFont(font)

        self.k_value_edit = QLineEdit(self)
        self.k_value_edit.move(250, 100)
        self.k_value_edit.setFont(font)


        self.m_value_label = QLabel("Введите число M:", self)
        self.m_value_label.move(20, 140)
        self.m_value_label.setFont(font)

        self.m_value_edit = QLineEdit(self)
        self.m_value_edit.move(250, 140)
        self.m_value_edit.setFont(font)


        self.generate_array_button = QPushButton("Сгенерировать массив", self)
        self.generate_array_button.move(20, 180)
        self.generate_array_button.setFont(font)
        self.generate_array_button.clicked.connect(self.generate_array)


        self.clear_form_button = QPushButton("Очистить форму", self)
        self.clear_form_button.move(300, 180)
        self.clear_form_button.setFont(font)
        self.clear_form_button.clicked.connect(self.clear_form)


        self.array_table = QTableWidget(self)
        self.array_table.move(20, 220)
        self.array_table.setFont(font)
        self.array_table.resize(400, 400)
        self.array_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.array_table.setVisible(False)

    def update_array_type(self):
        array_type = self.array_type_combo.currentText()
        if array_type == "Одномерный":
            self.array_dim_label.setVisible(True)
            self.array_dim_edit.setVisible(True)
        else:
            self.array_dim_label.setVisible(False)
            self.array_dim_edit.setVisible(False)

    def generate_array(self):
        array_type = self.array_type_combo.currentText()
        try:
            array_dim = int(self.array_dim_edit.text())
            k_value = int(self.k_value_edit.text())
            m_value = int(self.m_value_edit.text())
        except ValueError:
            msg = QMessageBox.critical(self, "Ошибка!", "Введите числа!")
            return

        if array_type == "Одномерный":
            array = [random.randint(100, 999) for i in range(array_dim)]

            intermediate_values = []
            for i in range(array_dim):
                check = array[i] % 10
                beforeChanges = array[i]
                if check == k_value:
                    array[i] //= m_value
                    intermediate_values.append(str(beforeChanges) + " -> " + str(array[i]))
                else:
                    intermediate_values.append(str(array[i]))


            self.array_table.clear()
            self.array_table.setColumnCount(2)
            self.array_table.setHorizontalHeaderLabels(["Значение", "Преобразование"])
            self.array_table.setRowCount(array_dim)
            self.array_table.setColumnWidth(0, 300)
            self.array_table.setColumnWidth(1, 300)
            self.array_table.resize(650, 650)

            for i in range(array_dim):
                original_value_item = QTableWidgetItem(str(array[i]))
                new_value_item = QTableWidgetItem(intermediate_values[i])
                if i % 2 == 0:
                    original_value_item.setBackground(Qt.lightGray)
                    new_value_item.setBackground(Qt.lightGray)
                self.array_table.setItem(i, 0, original_value_item)
                self.array_table.setItem(i, 1, new_value_item)

            self.array_table.setVisible(True)
            self.resize(900, 900)


    def clear_form(self):
        self.array_dim_edit.clear()
        self.k_value_edit.clear()
        self.m_value_edit.clear()
        self.array_table.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = ArrayProgram()
    program.setGeometry(100, 100, 500, 400)
    program.show()
    sys.exit(app.exec_())
