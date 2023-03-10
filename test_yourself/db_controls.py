import sqlite3
from test_yourself import app
from flask import g


def add_new_test(question, ans1, ans2, correct):
    msg = ""
    try:
        with sqlite3.connect("app.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO drivers_test
            (question, ans1, ans2, correct) VALUES 
            (?, ?, ?, ?)""", (question, ans1, ans2, correct))
            connection.commit()
            msg = "Succesfully added"
    except Exception as e:
        connection.rollback()
        msg = "Error"
    finally:
        connection.close()
        return msg


def get_db(table_name=None):
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        cursor = db.cursor()
        if table_name is None:
            all_data = cursor.execute("SELECT name FROM sqlite_schema WHERE type ='table'").fetchall()
        else:
            cursor.execute(f"select * from {table_name}")
            all_data = cursor.fetchall()
            all_data = [list(l) for l in all_data]
        return all_data


def delete_question(que):
    msg = ""
    try:
        with sqlite3.connect("app.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM drivers_test
            WHERE question = ? """, que)
            connection.commit()
            msg = "Successfully added"
    except Exception as e:
        connection.rollback()
        msg = "Error"
    finally:
        connection.close()
        return msg


def add_table(name):
    msg = ""
    try:
        with sqlite3.connect("app.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f'CREATE TABLE {name} (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)')
            connection.commit()
            msg = "Successfully added"
    except:
        connection.rollback()
        msg = "Error"
    finally:
        connection.close()
        return msg


def del_table(name):
    with sqlite3.connect("app.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f'DROP TABLE {name};')
        connection.commit()


@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
