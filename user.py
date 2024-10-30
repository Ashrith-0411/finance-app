from database import db
import hashlib

class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def register(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            user_id = db.cursor.lastrowid
            return User(user_id, username)
        except sqlite3.IntegrityError:
            return None

    @staticmethod
    def login(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = db.fetchone()
        if user:
            return User(user[0], username)
        return None