from database.user_repository import UserRepository
from models.session import Session

class SessionService:
    def __init__(self, db, user_repository: UserRepository):
        self.db = db
        self.user_repo = user_repository

    def save_session(self, user_id: int, duration: int):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sessions (user_id, duration) VALUES (?, ?)",
            (user_id, duration)
        )
        conn.commit()
        return cursor.lastrowid

    def get_sessions_for_user(self, user_id: int):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, user_id, duration, completed_at FROM sessions WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        return [Session(*row) for row in rows]
