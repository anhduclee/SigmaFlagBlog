import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("""CREATE TABLE users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL
             )""")
    c.execute("INSERT INTO users (username,password) VALUES('admin', '123')")
    conn.commit()
    conn.close()

def username_exists(username: str):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ?", (username, ))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

def signup(username: str, password: str):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login(username: str, password: str):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user_exists = c.fetchone()
    conn.close()
    if user_exists:
        return True
    return False