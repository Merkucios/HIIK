import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from FormFor5Lab import *
import numpy

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Button_Exit.clicked.connect(self.close)
        self.ui.Button_Count.clicked.connect(self.CountValue)
        self.ui.Button_New_Values.clicked.connect(self.RestartButtons)
        self.ui.Button_Save.clicked.connect(self.SaveValues)

        self.ui.Button_Count.setStyleSheet('background-color: green')
        self.ui.TableWidget.setColumnWidth(0, 200)
        self.ui.TableWidget.setColumnWidth(1, 200)

        self.ui.Button_Save.setDisabled(True)
        self.ui.Button_New_Values.setDisabled(True)

        self.ui.Button_Count.setToolTip('Производит вычисления по формулам\n-x^3+9\n-1/(x+1)')
        self.ui.Button_Save.setToolTip('Результат вычислений сохраняется в файл data.txt')
        self.ui.Button_New_Values.setToolTip('Ввод новых значений')

        header = self.ui.TableWidget.horizontalHeader()
        header.setStyleSheet("color: red;")

    def RestartButtons(self):
        self.ui.TableWidget.setRowCount(0)
        self.ui.Button_Save.setDisabled(True)
        self.ui.Button_New_Values.setDisabled(True)
        self.ui.Button_Count.setEnabled(True)
        self.ui.X_Start.setText('')
        self.ui.X_End.setText('')
        self.ui.Step.setText('')
        self.ui.TableWidget.clearContents()
        self.ui.X_Start.setEnabled(True)
        self.ui.X_End.setEnabled(True)
        self.ui.Step.setEnabled(True)


    def ErrorOccured(self):
        error_box = QtWidgets.QMessageBox.critical(self, "Значения", "Введите правильные значения!")

    def CountValue(self):
        if self.ui.X_Start.text() == '' or self.ui.X_End.text() == '' or self.ui.Step.text() == '':
            return self.ui.statusbar.showMessage('Введены неверные значения', 2000)
        try:
            self.row_counter = 0
            first_x = float(self.ui.X_Start.text())
            last_x = float(self.ui.X_End.text())
            step = float(self.ui.Step.text())
            if first_x > last_x:
                step = step * -1

            self.ui.Button_Count.setDisabled(True)
            self.ui.Button_Save.setEnabled(True)
            self.ui.Button_New_Values.setEnabled(True)



            for i in numpy.arange(first_x, last_x + 0.00001, step):
                if i <= 13:
                    self.ui.TableWidget.insertRow(self.row_counter)
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, str(round(pow(-i, 3) + 9, 2)))
                    self.ui.TableWidget.setItem(self.row_counter, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, str(round(i, 1)))
                    self.ui.TableWidget.setItem(self.row_counter, 1, item)
                elif i > 13:
                    self.ui.TableWidget.insertRow(self.row_counter)
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, str(round(-1 / (i + 1), 5)))
                    self.ui.TableWidget.setItem(self.row_counter, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, str(round(i, 1)))
                    self.ui.TableWidget.setItem(self.row_counter, 1, item)

                self.row_counter += 1

            self.ui.X_Start.setDisabled(True)
            self.ui.X_End.setDisabled(True)
            self.ui.Step.setDisabled(True)

        except ValueError:
            self.ErrorOccured()

    def SaveValues(self):
        try:
            file = open('values.txt', 'a', encoding='utf-8')
            file.write("F(X) ||| x\n")
            for i in range(self.row_counter):
                file.write(f'{self.ui.TableWidget.item(i, 0).text()} ||| '
                           f'{self.ui.TableWidget.item(i, 1).text()} \n')
            inf_box = QtWidgets.QMessageBox.information(self, "Результат", "Результат сохранён в values.txt")
            self.ui.Button_Save.setDisabled(True)
        except:
            error_box = QtWidgets.QMessageBox.critical(self, "Ошибка!", "Результат не сохранён в файл!")
        finally:
            file.close()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())