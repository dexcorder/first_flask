class UserService:
    def __init__(self):
        # In-memory user storage
        self.users = {}  # {'email': {'password': 'hashed_password'}}

    def user_exists(self, email):
        return email in self.users

    def add_user(self, email, hashed_password):
        self.users[email] = {'password': hashed_password}

    def get_user(self, email):
        return self.users.get(email)