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
    # connect_to_db()

    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username,))
    return DB.fetchone()[0]

def authenticate(username, password):
    query = """SELECT id, username, password FROM users WHERE username = ?"""
    DB.execute(query, (username, ))
    row = DB.fetchone()
  
    if username == row[1] and hash(password) == hash(row[2]):
        return row[0] # userid
    else:
        return None

# print authenticate("meghan", "urback")

def get_wall_posts(userid):
    # connect_to_db()
    query = """SELECT created_at, content FROM wall_posts WHERE owner_id = ?"""
    DB.execute(query, (userid, ))
    return DB.fetchall()
