import sqlite3

db = sqlite3.connect('db.db')
cursor = db.cursor()

def add_class(class_usr, nation):
    cursor.execute(f"SELECT class FROM users WHERE class = '{class_usr}'")
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{class_usr}', '{nation}')")
        db.commit()
        return 'OK'
    else:
        return 'ERROR'

def all():
    l = []
    for i in cursor.execute("SELECT * FROM users"):
        l.append(i)
    return l

def see():
    pass

all()
