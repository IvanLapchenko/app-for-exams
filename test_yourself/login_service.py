import sqlite3
from random import randint

from flask_login import UserMixin

connection = sqlite3.connect("app.db", check_same_thread=False)
cursor = connection.cursor()


def check_if_user_exists_return_object(name):
    cursor.execute(f"SELECT id from test WHERE log = '{name}'")
    password = cursor.fetchall() #this is here cause req returns list of tuples
    print(password)

    if len(password) == 0:
        return None

    return User(1, "a", 'a')


class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def get_id(self):
        return self.id