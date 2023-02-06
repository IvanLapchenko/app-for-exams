from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from test_yourself import app, db_controls, login_manager
from flask import render_template, request, redirect, flash
from test_yourself.login_service import *
from tests_service import *


@app.route("/index")
def index():
    return render_template("add_test.html")


@app.route("/add_test", methods=['GET', 'POST'])
@login_required
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
@app.route("/drivers_test/<specified_test>", methods=['GET', 'POST'])
def drivers_test(specified_test=None):
    correct, all_data = shuffle_answers_to_test(specified_test)

    if request.method == "POST":
        is_passed, correct_answers = count_correct_answers(correct, request.form)
        return render_template("see_result.html",
                               correct_answers=correct_answers,
                               passed=is_passed)

    return render_template("drivers_test.html", all_data=all_data)


@app.route("/add_new_topic", methods=['GET', 'POST'])
@login_required
def add_new_topic():
    all_topics = get_table_names_in_correct_format()

    if request.method == "POST":
        msg = db_controls.add_table(request.form["topic"])
        return render_template("add_new_topic.html", all_topics=all_topics, msg=msg)

    return render_template("add_new_topic.html", all_topics=all_topics)


@app.route("/delete_table/<name>")
@login_required
def delete_table(name):
    name = name.replace(" ", "_")
    db_controls.del_table(name)
    return redirect("/add_new_topic")


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        user_from_database = get_user_by_column("username", name)

        if user_from_database and check_password_hash(user_from_database.password, password):
            login_user(user_from_database)
            return redirect("drivers_test")

        flash("Check if you entered data correctly")
        return redirect("login")

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("login")


@login_manager.user_loader
def load_user(user_id):
    user = get_user_by_column("id", user_id)
    return user