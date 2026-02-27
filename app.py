from flask import Flask, request, render_template, redirect, url_for, session, flash
import database

app = Flask(__name__)
app.config["SECRET_KEY"] = "imissher"

database.init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmed_password = request.form.get("confirm")
        if password != confirmed_password:
            return render_template("signup.html")
        elif database.username_exists(username):
            return render_template("signup.html")
        else:
            database.signup(username,password)
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if database.login(username, password):
            session["user"] = username
            return redirect(url_for("user"))
        else:
            return render_template("login.html")
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
    

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user")
    return redirect(url_for("home"))

@app.route("/user")
def user():
    if "user" in session:
        return render_template("user.html", user = session["user"])
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)