import sqlite3

connection = sqlite3.connect("app.db", check_same_thread=False)
cursor = connection.cursor()


def check_if_user_exists_return_password(name):
    cursor.execute(f"SELECT pwd from test WHERE log = '{name}'")
    password = cursor.fetchall()[0][0] #this is here cause req returns list of tuples
    if len(password) == 1: password = None
    return password
