from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/error_test_500', methods=['POST'])
def error_test_500():
    post = request.json[0]
    return len(post.get('C'))


@app.route('/')
def hello():
    return 'hello1111'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111, debug=False)
