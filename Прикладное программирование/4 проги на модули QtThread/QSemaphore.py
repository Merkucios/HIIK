from PyQt5.QtCore import QSemaphore
import sqlite3


class Database:
    # TODO: База данных под создание
    def __init__(self):
        try:
            self.name = None
            self.dbsemaphore = QSemaphore(1)  # Контроль БД
            self.dbname = r"D:/SQLite/DataBases/" + str(self.name)

        except (Exception) as err:
            print("[-] Не получилось создать БД.", err)

    def openDB(self, dbfilename):
        try:
            self.name = dbfilename
            self.dbname = r"D:/SQLite/DataBases/" + str(dbfilename)
            sql_con = sqlite3.connect(self.dbname)
            return sql_con
        except (TypeError) as err:
            print("[-] Не получилось создать БД.", err)

    def commit(self):
        self.dbsemaphore.acquire()
        self.dbsemaphore.release()


if __name__ == "__main__":
    db = Database()
    db.name = "mydatabase142.db"
    chkc = db.openDB(db.name)
    db.commit()