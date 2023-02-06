import sqlite3
from flask_login import UserMixin


connection = sqlite3.connect("app.db", check_same_thread=False)
cursor = connection.cursor()


def get_user_by_column(column: str, value: any) -> object | None:
    cursor.execute(f"SELECT * from users WHERE {column} = '{value}'")
    if check_if_user_found(cursor.fetchall()):
        id, username, password = cursor.fetchall()[0]
        return User(id, username, password)


def check_if_user_found(data: list) -> bool:
    return True if len(data) > 0 else False


class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def get_id(self):
        return self.id