import sqlite3
from flask import session
from datetime import date

def createDB(): #This initially creates sql database, only need to run once
    try:
        conn = sqlite3.connect("post.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE posts
                    (
                    id TEXT,
                    owner TEXT,
                    content TEXT,
                    date DATE
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
        conn = sqlite3.connect("post.db")
        c = conn.cursor()
        for row in c.execute("SELECT * FROM posts"):
            print(row)
    except Exception as e:
        print(e)
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def addPosts(id, owner, content, timestamp):
    dataToInsert = [(id, owner, content, timestamp)]
    try:
        conn = sqlite3.connect("post.db")
        c = conn.cursor()
        c.executemany("INSERT INTO posts VALUES (?, ?, ?, ?)", dataToInsert)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Tried to duplicate record")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def getPosts():
    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        c.executemany("SELECT owner, content, timestamp FROM posts WHERE timestamp ")
    except Exception as e:
        return(e)
# createDB()
# addPosts("id","TestUSER","Some type of string content for our db", date.today())
displayDB()