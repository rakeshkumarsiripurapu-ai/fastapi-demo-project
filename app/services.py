users = []

def get_users():
    return users

def create_user(user: dict):
    users.append(user)
    return user
