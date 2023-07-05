import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlTableModel

from mainform import Ui_MainWindow
from dialogform import Ui_Dialog
from connection import Data

class Vostok_Service(QMainWindow):
    def __init__(self):
        super(Vostok_Service, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.btn_new_zakaz.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_change_data.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_delete_zakaz.clicked.connect(self.delete_current_transaction)

        self.ui.label_balance.setText(self.conn.total_balance())
        self.ui.income_balance.setText(self.conn.total_income())
        self.ui.outcome_balance.setText(self.conn.total_outcome())

        self.ui.balance_exoskeleton.setText(self.conn.total_exoskelet())
        self.ui.balance_odeshda.setText(self.conn.total_spesodeshda())
        self.ui.balance_other.setText(self.conn.total_other())
        self.ui.balance_obyv.setText(self.conn.total_spesobyv())
        self.ui.balance_ryki.setText(self.conn.total_zashit_ryk())
        self.ui.balance_sredstva_zashit.setText(self.conn.total_sredstva_zashit())
        self.ui.balance_vending.setText(self.conn.total_vending())

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Новый заказ":
            self.ui_window.btn_transaction.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.btn_transaction.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        date = self.ui_window.date.text()
        category = self.ui_window.cb_category.currentText()
        description = self.ui_window.le_description.text()
        balance = self.ui_window.le_balance.text()
        status = self.ui_window.cb_typebudget.currentText()

        self.conn.add_new_transaction_query(date, category, description, balance, status)
        self.view_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.date.text()
        category = self.ui_window.cb_category.currentText()
        description = self.ui_window.le_description.text()
        balance = self.ui_window.le_balance.text()
        status = self.ui_window.cb_typebudget.currentText()

        self.conn.update_transaction_query(date, category, description, balance, status, id)
        self.view_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delete_transaction_query(id)
        self.view_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vostok_Service()
    window.show()

    sys.exit(app.exec_())
