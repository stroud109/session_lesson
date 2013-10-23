from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/", methods=['GET'])
def index():
    if session.get("username"):
        return redirect(url_for("view_user", username=session.get("username")))
    else: 
        return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user_id = model.authenticate(username, password)
    if user_id != None:
        flash("User authenticated!")
        session['username'] = username
    else:
        flash("Password incorrect, there may be a ferret stampede in progress!")
    
    return redirect(url_for("index"))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for("index"))

@app.route("/user/<username>")
def view_user(username):
    model.connect_to_db()
    user_id = model.get_user_by_name(username)
    posts = model.get_wall_posts(user_id)
    return render_template("wall.html", the_posts=posts, username=username)



if __name__ == "__main__":
    app.run(debug = True)


