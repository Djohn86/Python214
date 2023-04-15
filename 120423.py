import sqlite3


# con = sqlite3.connect('profile.db')
# cur = con.cursor()
#
# con.close()

with sqlite3.connect('profile.db') as con:
    cur = con.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS users(
    # id  INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # summa REAL,
    # data TEXT
    # )''')

    cur.
