import sqlite3

conn = sqlite3.connect("expenses.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY, 
Date DATE,
decription TEXT,
category TEXT,
price REAL)""")

conn.commit()
conn.close()