import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_methods")
def get_methods():
    methods = list(mongo.db.methods.find())
    methods.reverse()
    return render_template("methods.html", methods=methods)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("sign_up"))

        if request.form.get("password") == request.form.get(
                "password_confirm"):
            sign_up = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(sign_up)

            # put the new user into session cookie
            session["user"] = request.form.get("username").lower()
            flash("Sign-Up Successful!")
            return redirect(url_for("profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in db.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check hashed passwords match
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # When passwords dont match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # When username provided not present in DB.
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the DB, for display on the page.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove the user from the session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_method", methods=["GET", "POST"])
def add_method():
    if request.method == "POST":
        todaysDate = date.today()
        euroDate = todaysDate.strftime("%d/%m/%Y")
        method = {
            "method_name": request.form.get('method_name'),
            "category_name": request.form.get('category_name'),
            "method_description": request.form.get('method_description'),
            "method_video": request.form.get('method_video'),
            "method_steps": request.form.get('method_steps'),
            "method_created": euroDate,
            "created_by": session["user"]
        }
        mongo.db.methods.insert_one(method)
        flash("DIY Method Successfully Added")
        return redirect(url_for("get_methods"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_method.html", categories=categories)


@app.route("/method/<method_id>", methods=["GET"])
def method(method_id):
    method = mongo.db.methods.find_one({"_id": ObjectId(method_id)})
    return render_template("method.html", method=method)


@app.route("/method/edit_method/<method_id>", methods=["GET", "POST"])
def edit_method(method_id):
    method = mongo.db.methods.find_one({"_id": ObjectId(method_id)})
    if request.method == "POST":
        edit = {
            "method_name": request.form.get('method_name'),
            "category_name": request.form.get('category_name'),
            "method_description": request.form.get('method_description'),
            "method_video": request.form.get('method_video'),
            "method_steps": request.form.get('method_steps'),
            "created_by": session["user"]
        }
        mongo.db.methods.update({"_id": ObjectId(method_id)}, edit)
        flash("DIY Method Successfully Updated")
        return render_template("method.html", method=method)

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_method.html", method=method, categories=categories)


@app.route("/delete_method/<method_id>")
def delete_method(method_id):
    mongo.db.methods.remove({"_id": ObjectId(method_id)})
    flash("Method Successfully Deleted")
    return redirect(url_for("get_methods"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # UPDATE TO DEBUG=FALSE BEFORE FINAL SUBMISSION!!!!!!
            debug=True)
