import sqlite3

from werkzeug.security import generate_password_hash

connection = sqlite3.connect('app.db')
print("Opened database successfully")

# connection.execute('CREATE TABLE drivers_test (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)')

connection.execute("""INSERT INTO users (username, password) VALUES  (?, ?)""", ("user1", generate_password_hash("user1")))

# connection.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
connection.commit()
print("Table created successfully ")
connection.close()


