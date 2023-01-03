import sqlite3

connection = sqlite3.connect('app.db')
print("Opened database successfully")

connection.execute('CREATE TABLE drivers_test (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)')
print("Table created successfully ")
connection.close()


