from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return ("Index Page")


@app.route('/hello')
def hello():
    return 'Hello Page'


@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username=None):
    # show the user profile for that user
    if username == None:
        username = "aaa"
    return f'User {(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/hello2/<name>')
def hello2(name=None):
    return render_template('hello2.html', name=name)


if __name__ == '__main__':
    app.run(host="0.0.0", port=5000, debug=True)
