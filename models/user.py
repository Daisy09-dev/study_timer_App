class User:
    def __init__(self, user_id: int = None, name: str = ""):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}')"
