import sqlite3

from flask_login import UserMixin

connection = sqlite3.connect("app.db", check_same_thread=False)
cursor = connection.cursor()


def get_user_by_id(user_id):
    cursor.execute(f"SELECT * from users WHERE id = '{user_id}'")
    id, username, password = cursor.fetchall()[0]
    return User(id, username, password)

def check_if_user_exists_return_object(name):
    cursor.execute(f"SELECT * from users WHERE username = '{name}'")

    # if len(user_data) == 0:
    #     return None

    id, username, password = cursor.fetchall()[0]
    print(id, username, password)
    return User(id, username, password)


class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def get_id(self):
        return self.id