from flask import session
import sqlite3
import os
import binascii
import hashlib

def createDB(): #This initially creates sql database, only need to run once
    try:
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                    (
                    id TEXT,
                    username TEXT,
                    password TEXT,
                    score TEXT
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

def saltPassword(password) -> str: #Cybersecurity (only backend)
    salt = os.urandom(40)
    salt = binascii.hexlify(salt).decode()
    hashable = salt + password
    hashable = hashable.encode('utf-8')
    this_hash = hashlib.sha1(hashable).hexdigest()
    return salt + this_hash

def addUser(id, username, password, score): #Adds user to database (endpoint)
    saltedPassword = saltPassword(password)
    dataToInsert = [(id, username, saltedPassword, score)]
    try:
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        c.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", dataToInsert)
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

def authenticateUser(username, password, saltLength=None) -> bool: #Authenticates user (endpoint)
    try:
        saltLength = saltLength or 80
        stored = getUserInfo(username) #Grabs password from database
        salt = stored[:saltLength] #Retrieves salt
        storedHash = stored[saltLength:] #Retrieves salted password
        hashable = salt + password
        hashable = hashable.encode('utf-8')
        thisHash = hashlib.sha1(hashable).hexdigest()
        return thisHash == storedHash #Compares generated and stored
    except:
        print("Could not retrieve password from username")
        return False

def getUserInfo(username) -> str: #Gets either password for given username (only backend)
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = '" + username + "'")
    r = c.fetchall()
    for i in r:
        if username == i[1]: #username
            return i[2] #password
        else:
            return "Could not get password from database"

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