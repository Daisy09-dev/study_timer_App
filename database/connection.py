import sqlite3
import os

class DatabaseConnection:
    def __init__(self, db_name="study_timer.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        """Establish database connection."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def initialize(self):
        """Create required tables if they don’t exist."""
        conn = self.connect()
        cursor = conn.cursor()

        # User table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        # Session table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                duration INTEGER,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)

        conn.commit()

    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
        print("Database connection closed.")