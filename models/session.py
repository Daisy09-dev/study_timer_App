class Session:
    def __init__(self, session_id: int = None, user_id: int = None, duration: int = 0, completed_at: str = None):
        self.session_id = session_id
        self.user_id = user_id
        self.duration = duration  # in minutes
        self.completed_at = completed_at

    def __repr__(self):
        return f"Session(id={self.session_id}, user_id={self.user_id}, duration={self.duration}, completed_at={self.completed_at})"
