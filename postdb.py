import sqlite3
from flask import session

def createDB(): #This initially creates sql database, only need to run once
    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                    (
                    id = TEXT,
                    owner = TEXT,
                    content = TEXT,
                    timeStamp = TEXT,
                    )''')
        conn.commit()
        return True
    except BaseException:
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def displayDB(): #Displays database for debugging
    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        for row in c.execute("SELECT * FROM posts"):
            print(row)
    except sqlite3.DatabaseError:
        print("Error. Could not retrieve data")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def addPosts(id, owner, content, timestamp):
    dataToInsert = [(id, owner, content, timestamp)]
    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        c.executemany("INSERT INTO posts VALUES (?, ?, ?, ?)", dataToInsert)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Tried to duplicate record")
    else:
        session['invalidLogin'] = "Success!"
        print("Success")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()