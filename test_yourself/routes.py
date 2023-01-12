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
    all_data = db_controls.get_db()
    if request.method == "POST":
        return request.form
    return render_template("drivers_test.html", all_data=all_data)


# @app.route("/view_test", methods=['GET', 'POST'])
# def view_test():
#     all_data = db_controls.get_db()
#     if request.method == "POST":
#         answers.append(request.form["check"])
#     return render_template("drivers_test.html", all_data=all_data)