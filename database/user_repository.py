from .connection import DatabaseConnection

class UserRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_user(self, name: str):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        return cursor.lastrowid

    def get_user(self, user_id: int):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

    def get_all_users(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users")
        return cursor.fetchall()
