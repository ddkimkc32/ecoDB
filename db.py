from flask import session
import sqlite3

def createDB(): #This initially creates sql database, only need to run once
    try:
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                    (
                    username TEXT,
                    password TEXT,
                    score INTEGER
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

def addUser(username, password, score): #Adds user to database
    dataToInsert = [(username, password, score)]
    try:
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        c.executemany("INSERT INTO users VALUES (?, ?, ?)", dataToInsert)
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

def displayDB(): #Displays database for debugging
    try:
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        for row in c.execute("SELECT * FROM users"):
            print(row)
    except sqlite3.DatabaseError:
        print("Error. Could not retrieve data")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

displayDB()