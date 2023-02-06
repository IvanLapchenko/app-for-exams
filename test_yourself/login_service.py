import sqlite3
from flask_login import UserMixin


connection = sqlite3.connect("app.db", check_same_thread=False)
cursor = connection.cursor()


def get_user_by_column(column: str, value: any) -> object | None:
    cursor.execute(f"SELECT * from users WHERE {column} = '{value}'")
    user_data_list = cursor.fetchall()
    if check_if_user_found(user_data_list):
        (id, username, password) = user_data_list[0]
        return User(id, username, password)
    return None


def check_if_user_found(data: list) -> bool:
    print(len(data))
    print(data)
    return True if len(data) > 0 else False


class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def get_id(self):
        return self.id