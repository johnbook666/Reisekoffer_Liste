from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

koffer_list = ["Flug + Bahntickets", "Bargeld", "Wäsche"]

# GET ROUTES

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    # get posts from database
    return render_template("posts.html", posts=koffer_list)

@app.route("/enter-post")
def enter_post():
    return render_template("add-posts.html")

@app.route("/about")
def about():
    posts = []
    koffer_list = []
    return render_template("about.html")

# POST ROUTES

@app.route("/add-post", methods=["POST"])
def add_post():
    new_post = request.form.get("title")
    # add post to database
    koffer_list.append(new_post)
    return redirect("/posts")


if __name__ == '__main__':
    app.run()