import sqlite3
from random import randint

connection = sqlite3.connect("app.db", check_same_thread=False)
cursor = connection.cursor()


def check_if_user_exists_return_password(name):
    cursor.execute(f"SELECT pwd from test WHERE log = '{name}'")
    password = cursor.fetchall()[0][0] #this is here cause req returns list of tuples
    if len(password) == 1: password = None
    return password


class User():
    def __init__(self, name, password):
        id = randint(10000, 99999)
        self.name = name
        self.password = password