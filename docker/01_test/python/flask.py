from flask import Flask
from flask_cors import CORS
import sys

print(sys.path)


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return ("hello")


@app.route("/aa")
def hello2():
    return ("hello2")


@app.route('/test01/')
def test01():
    return 'test01'


@app.route('/test01/22/')
def test012():
    return 'test01'


@app.route('/test02')
def test02():
    return 'test02'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
