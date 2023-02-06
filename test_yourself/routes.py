import sqlite3
from random import randint
from werkzeug.security import generate_password_hash
from test_yourself import app, db_controls
from flask import render_template, request, redirect



@app.route("/index")
def index():
    return render_template("add_test.html")


@app.route("/add_test", methods=['GET', 'POST'])
def add_test():
    if request.method == "POST":
        question = request.form["question"]
        ans1 = request.form["ans1"]
        ans2 = request.form["ans2"]
        correct = request.form["correct"]
        res = db_controls.add_new_test(question, ans1, ans2, correct)
        return res
    return render_template("add_test.html")


@app.route("/drivers_test")
@app.route("/drivers_test/<specified>", methods=['GET', 'POST'])
def drivers_test(specified=None):
    if specified: specified = specified.replace(" ", "_")
    all_data = db_controls.get_db(specified)
    correct = {i[0]: i[3] for i in all_data}
    [test.insert(randint(1, 3), test.pop(3)) for test in all_data]
    if request.method == "POST":
        correct_answers = 0
        passed = False
        for i in correct:
            if request.form[i] == correct[i]:
                correct_answers += 1
            if correct_answers / len(correct) > 0.75:
                passed = True
        return render_template("see_result.html", correct_answers=correct_answers, passed=passed)
    return render_template("drivers_test.html", all_data=all_data)


@app.route("/add_new_topic", methods=['GET', 'POST'])
def add_new_topic():
    all_topics = db_controls.get_db()
    all_topics = [str(i[0]).replace("_", " ") for i in all_topics]
    if request.method == "POST":
        msg = db_controls.add_table(request.form["topic"])
        return render_template("add_new_topic.html", all_topics=all_topics, msg=msg)
    return render_template("add_new_topic.html", all_topics=all_topics)


@app.route("/delete_table/<name>")
def delete_table(name):
    name = name.replace(" ", "_")
    db_controls.del_table(name)
    return redirect("/add_new_topic")


# @app.route("/")
# @app.route("/test", methods=["GET", "POST"])
# def test():
#     if request.method == "POST":
#         log = request.form["log"]
#         pwd = generate_password_hash(request.form["pwd"])
#         con = sqlite3.connect("app.db")
#         con.execute(f"INSERT INTO test (log, pwd) VALUES {log, pwd}")
#         con.commit()
#         return pwd
#     return render_template("test.html")