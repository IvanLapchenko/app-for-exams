from test_yourself import app


@app.route('/home')
@app.route("/")
def home():
    return "Hello world!"
