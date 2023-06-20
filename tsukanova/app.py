from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

menu = ["first", "second", "more"]


@app.route("/")
def index():
    return render_template("index.html", title="MEGA TITLE", h1="MEGA H1", menu=menu)


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "user: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)


