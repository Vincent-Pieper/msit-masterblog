from flask import Flask, render_template
import storage


DATA = "data/blog_posts.json"


app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = storage.get_json(DATA)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)