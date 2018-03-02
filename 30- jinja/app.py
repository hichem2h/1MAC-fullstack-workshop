from flask import Flask, render_template
from dummy_data import post_store

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    posts = post_store.get_all()
    return render_template('index.html', posts = posts)


if __name__ == '__main__':
    app.run()
