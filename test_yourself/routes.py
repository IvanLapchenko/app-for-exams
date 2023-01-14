from random import randint

from test_yourself import app, db_controls
from flask import render_template, request


@app.route("/")
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


@app.route("/drivers_test", methods=['GET', 'POST'])
def drivers_test():
    all_data = db_controls.get_db("drivers_test")
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
        return msg
    return render_template("add_new_topic.html", all_topics=all_topics)


