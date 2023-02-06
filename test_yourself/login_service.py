import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()


def check_if_user_exists_return_password(name):
    cursor.execute(f"SELECT password from test WHERE pwd = {name}")

    return cursor.fetchall()