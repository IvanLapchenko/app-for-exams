from flask import Flask

app = Flask(__name__)

from test_yourself import routes

if __name__ == '__main__':
    app.run()
