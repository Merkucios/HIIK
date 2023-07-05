import sqlite3

def sqlite_output(cur, sql_command):
    for row in cur.execute(sql_command).fetchall():
        print(row)


try:
    con = sqlite3.connect(":memory:")
except sqlite3.DatabaseError as err:
    print(f"Ошибка подключения к БД : {err}")
else:
    print("Успешно подключена база данных")

cur = con.cursor()
sql_create = """ 
    CREATE TABLE IF NOT EXISTS homework (uni INTEGER UNIQUE ON CONFLICT ROLLBACK, t TEXT);
             """
cur.executescript(sql_create)

sql_uniq_check = """
    SELECT sql FROM sqlite_master WHERE TYPE = "table" and NAME = "homework";
                 """
sqlite_output(cur, sql_uniq_check)

cur.close()
con.close()
print("Соединение с базой данных успешно завершено")
input()


