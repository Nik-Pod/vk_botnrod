import sqlite3

db = sqlite3.connect('db.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    class TEST,
    nation TEXT
)""")

db.commit()
