from flask import Flask
from flask_cors import CORS  # need to mention
import json
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def json_file():
    # file_path = os.path.join(os.getcwd(), 'backend', 'data.json')
    file_path = './data.json'
    with open(file_path) as file:
        return json.load(file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)
