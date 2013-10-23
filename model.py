# ADMIN_USER="hackbright"
# ADMIN_PASSWORD=5980025637247534551
import sqlite3

CONN = None
DB = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()


def get_user_by_name(username):
    connect_to_db()
    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username,))
    return DB.fetchone()[0]

def authenticate(username, password):
    connect_to_db()
    query = """SELECT id, username, password FROM users WHERE username = ?"""
    DB.execute(query, (username, ))
    row = DB.fetchone()

    if row and username == row[1] and hash(password) == hash(row[2]):
        return row[0] # userid
    else:
        return None

def create_wall_post(the_owner_id, the_author_id, the_content):
    connect_to_db()
    query = """INSERT INTO wall_posts (owner_id, author_id, created_at, content) VALUES (?, ?, CURRENT_DATE, ?)"""
    DB.execute(query,(the_owner_id, the_author_id, the_content))
    CONN.commit()

def get_wall_posts(userid):
    connect_to_db()
    query = """SELECT created_at, content FROM wall_posts WHERE owner_id = ?"""
    DB.execute(query, (userid, ))
    return DB.fetchall()

