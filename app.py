from flask import Flask, render_template, request, redirect, url_for
import storage


DATA = "data/blog_posts.json"


app = Flask(__name__)


@app.route("/")
def index():
    """Display all blog posts on the homepage."""
    blog_posts = storage.get_json(DATA)
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Display the add form and save a new blog post."""
    if request.method == "POST":
        new_input = request.form.to_dict()
        blog_posts = storage.get_json(DATA)
        new_id = storage.get_available_id(blog_posts)
        new_blogpost = storage.create_new_blogpost(new_input, new_id)
        blog_posts.append(new_blogpost)

        if new_id != len(blog_posts):
            storage.reorder_blogposts_by_id(blog_posts)
        storage.save_json(DATA, blog_posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """Delete a blog post by its ID and redirect to the homepage."""
    blog_posts = storage.get_json(DATA)
    storage.delete_blogpost_by_id(blog_posts, post_id)
    storage.save_json(DATA, blog_posts)
    return redirect(url_for('index'))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Display the update form and save changes to an existing blog post."""
    blog_posts = storage.get_json(DATA)
    post = storage.fetch_blogpost_by_id(blog_posts, post_id)
    if not post:
        return "Post not found", 404

    if request.method == 'POST':
        updates = request.form.to_dict()
        storage.update_blogpost_by_id(blog_posts, post_id, updates)
        storage.save_json(DATA, blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)