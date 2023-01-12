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


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        cursor = db.cursor()
        cursor.execute("select * from drivers_test")
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
            msg = "Succesfully added"
    except Exception as e:
        connection.rollback()
        msg = "Error"
    finally:
        connection.close()
        return msg


@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
