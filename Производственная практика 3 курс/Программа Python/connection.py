from PyQt5 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database_tovar.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не могу открыть базу данных",
                                           "Нажмите \"Отменить\" для выхода из программы.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '₽'

        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")

    def total_income(self):
        return self.get_total(column="Balance", filter="Status", value="Доход")

    def total_outcome(self):
        return self.get_total(column="Balance", filter="Status", value="Расход")

    def total_spesodeshda(self):
        return self.get_total(column="Balance", filter="Category", value="Спецодежда")

    def total_spesobyv(self):
        return self.get_total(column="Balance", filter="Category", value="Спецобувь")

    def total_sredstva_zashit(self):
        return self.get_total(column="Balance", filter="Category", value="Средства защиты")

    def total_zashit_ryk(self):
        return self.get_total(column="Balance", filter="Category", value="Защита рук")

    def total_vending(self):
        return self.get_total(column="Balance", filter="Category", value="Вендинг")

    def total_exoskelet(self):
        return self.get_total(column="Balance", filter="Category", value="Экзоскелеты")

    def total_other(self):
        return self.get_total(column="Balance", filter="Category", value="Другое")