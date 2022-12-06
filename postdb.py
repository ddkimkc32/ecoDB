import datetime
import sqlite3

def createDB(): #This initially creates sql database, only need to run once
    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE posts
                    (
                    id INTEGER,
                    owner TEXT,
                    content TEXT,
                    timestamp TIMESTAMP
                    );''')
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

def addPosts(id, owner, content):
    timestamp = datetime.datetime.now()

    dataToInsert = [(id, owner, content, timestamp)]
    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()
        c.executemany("INSERT INTO posts VALUES (?, ?, ?, ?)", dataToInsert)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Tried to duplicate record")
    else:
        print("Success")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def sortPosts():
    # Sorts from newest to oldest, returns array of posts as dictionary and prints it out for debugging
    #DESC for newest to oldest, ASC for oldest to newest
    posts = [{}]

    try:
        conn = sqlite3.connect("posts.db")
        c = conn.cursor()

        for row in c.execute("SELECT * FROM posts ORDER BY timestamp DESC"):
            posts.append({'id':row[0], 'owner':row[1], 'content':row[2], 'timestamp':row[3]})
            print(row)
    except sqlite3.DatabaseError:
        print("Could not sort data")
    else:
        print("Sorted")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

    return posts



