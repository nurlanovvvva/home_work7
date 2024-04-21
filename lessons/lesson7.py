# SQL - язык структурированных запросов
# база данных -
# СУБД- система управления базами данных
# NOsql:SQL
# posgreSQL,mySQL, SQLite3-2

import sqlite3

# CRUD - create reed update delete
db = sqlite3.connect('op36_3.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
lastname TEXT,
age INTEGER,
view INTEGER,
bitday DATE
)''')


def delete_rows(condition):
    cursor.execute(f"DELETE FROM user WHERE {condition}")
    db.commit()
# UPDATE-UPDATE
cursor.execute('''UPDATE user SET age=99 WHERE rowid!=2 ''')

delete_rows("rowid % 2 = 0")

cursor.execute("SELECT rowid, * FROM user")
rows = cursor.fetchall()
print("После удаления:")
for row in rows:
    print(row)

db.commit()
db.close()
