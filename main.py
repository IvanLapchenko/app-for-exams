# from flask import Flask, render_template, request
# import sqlite3
#
# app = Flask(__name__)
#
#
# @app.route('/enternew')
# def new_student():
#     return render_template('student.html')
#
#
# @app.route('/addrec', methods=['POST', 'GET'])
# def addrec():
#     msg = ""
#     if request.method == 'POST':
#         try:
#             nm = request.form['nm']
#             addr = request.form['add']
#             with sqlite3.connect("database.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO students (name,addr) VALUES (?,?)", (nm, addr))
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#             con.rollback()
#             msg = "error in insert operation"
#         finally:
#             con.close()
#             return render_template("result.html", msg=msg)
#
#
# @app.route('/home')
# @app.route("/")
# def home():
#     return render_template('home.html')
#
#
# @app.route('/list')
# def list():
#     con = sqlite3.connect("database.db")
#     con.row_factory = sqlite3.Row
#
#     cur = con.cursor()
#     cur.execute("select * from students")
#
#     rows = cur.fetchall()
#     return render_template("list.html", rows=rows)
#
#
# if __name__ == '__main__':
#     app.run()
# list = ["a", "b", "c", "d"]
# list_test = []
# from random import randint
# for i in range(5):
#     list_test.append(list)
# print(list_test)
# nl = []
#
# [l.insert(randint(1, 3), l.pop(3)) for l in list_test]
# for l in list_test:
#     print(l)
#     l.insert(randint(1, 3), l.pop(3))
#     nl.append(l)
#
#
# # print(all_data)
# print(list_test, 'lt')
# print(nl)





def remove(string):
    string = string.replace(",", "")
    string = string.replace(" ", "")
    return string


st = "О, гомін німого"
st = st.lower()
st = remove(st)
print(st)
print(st[::-1])
print(st == st[::-1])
















