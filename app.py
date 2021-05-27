import os
from flask import (Flask, flash, render_template,
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
@app.route("/methods")
def get_methods():
    methods = list(mongo.db.methods.find())
    methods.reverse()
    return render_template("methods.html", methods=methods)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    if not query:
        flash("Please enter something in the search bar")
        return redirect(url_for("get_methods"))
    methods = list(mongo.db.methods.find({"$text": {"$search": query}}))
    methods.reverse()
    return render_template("methods.html", methods=methods)


def is_signup_form_valid(form):
    username = form.get("username").lower()
    password = form.get("password")
    confirm_password = form.get("password_confirm")
    if not username or not password or not confirm_password:
        return False
    if len(username) < 5 or len(password) < 5 or len(confirm_password) < 5:
        return False
    if len(username) > 15 or len(password) > 15 or len(confirm_password) > 15:
        return False
    if password != confirm_password:
        return False
    return True


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("sign_up"))

        is_valid = is_signup_form_valid(request.form)

        if is_valid:
            sign_up = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "is_admin": False
            }
            mongo.db.users.insert_one(sign_up)

            # put the new user into session cookie
            session["user"] = request.form.get("username").lower()
            flash("Sign-Up Successful!")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Please enter the form values correctly")
            return redirect(url_for("sign_up"))

    logged_out = not session
    if logged_out:
        return render_template("sign_up.html")

    else:
        flash("You are already logged in! If you want to make another account, log out first")
        return redirect(url_for("get_methods"))


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
                return redirect(url_for("get_methods"))

        else:
            # When username provided not present in DB.
            flash("Incorrect Username and/or Password")
            return redirect(url_for("get_methods"))

    logged_out = not session
    if logged_out:
        return render_template("login.html")

    else:
        flash("You are already logged in!")
        return redirect(url_for("get_methods"))


@app.route("/profile")
def profile():
    try:
        # grab the session user's username from the DB,
        # for display on the page.
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        is_admin = mongo.db.users.find_one(
            {"username": session["user"]})["is_admin"]
        methods = list(mongo.db.methods.find())
        methods.reverse()
        myMethods = []
        for method in methods:
            if (method["created_by"]).lower() == (session["user"]).lower():
                myMethods.append(method)

        if session["user"]:
            return render_template("profile.html", username=username,
                                   categories=categories, is_admin=is_admin,
                                   myMethods=myMethods)
        else:
            return redirect(url_for("get_methods"))
    except:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove the user from the session cookie
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for("get_methods"))


def is_method_form_valid(form):
    method_name = form.get("method_name")
    method_description = form.get("method_description")
    method_steps = form.get("method_steps")
    if not method_name or not method_description or not method_steps:
        return False
    if (len(method_name) or len(method_description) or len(method_steps)) < 5:
        return False
    if len(method_name) > 50:
        return False
    if len(method_description) > 200:
        return False
    if len(method_steps) > 2000:
        return False
    return True


@app.route("/method/add", methods=["GET", "POST"])
def add_method():
    if request.method == "POST":
        todaysDate = date.today()
        euroDate = todaysDate.strftime("%d/%m/%Y")
        is_valid = is_method_form_valid(request.form)

        if is_valid:
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

        else:
            flash("Please enter the form values correctly")
            return redirect(url_for("add_method"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    # To prevent non-authorised users accessing the add method page,
    # I have included a check for a user session variable.
    # There may be a better way of doing this.
    if session and session['user']:
        return render_template("add_method.html", categories=categories)
    else:
        flash("To create a method, you must first log in.")
        return redirect(url_for("get_methods"))


def generate_embed_link_from_youtube_link(yt_link):
    # The following is a custom method that changes YouTube links
    # into the embed format that the iframe element that youtube
    # provides expects. To create it I extended the functionality
    # of a method found here, to make it work with links that users
    # may copy paste from their browser's search bar and sharing
    # links:
    # https://stackoverflow.com/questions/29781974/convert-youtube-link-into-an-embed-link/29782133
    videoUrl = yt_link
    watchV = "watch?v="
    channel = "&ab_channel="
    share = "tu.be/"
    if watchV in videoUrl:
        videoUrl = videoUrl.replace(watchV, "embed/")
    if channel in videoUrl:
        delString = videoUrl.split("&ab_channel=", 1)[1]
        videoUrl = videoUrl.replace(delString, "")
        videoUrl = videoUrl.replace(channel, "")
    if share in videoUrl:
        videoUrl = videoUrl.replace(share, "tube.com/embed/")
    return videoUrl


@app.route("/method/<method_id>/view", methods=["GET"])
def method(method_id):
    try:
        method = mongo.db.methods.find_one({"_id": ObjectId(method_id)})
        videoUrl = generate_embed_link_from_youtube_link(
            method["method_video"])
        if session:
            is_admin = mongo.db.users.find_one(
                {"username": session["user"]})["is_admin"]
            return render_template("method.html", method=method,
                                   videoUrl=videoUrl, is_admin=is_admin)
        else:
            return render_template(
                "method.html", method=method, videoUrl=videoUrl)
    except:
        flash("That method does not exist.")
        return redirect(url_for('get_methods'))


@app.route("/method/<method_id>/edit", methods=["GET", "POST"])
def edit_method(method_id):
    try:
        method = mongo.db.methods.find_one({"_id": ObjectId(method_id)})
        if request.method == "POST":
            is_valid = is_method_form_valid(request.form)
            if is_valid:
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
                return redirect(url_for('method', method_id=method_id))
            else:
                flash("Please enter form fields correctly")
                return redirect(url_for('method', method_id=method_id))

        if session:
            if method["created_by"].lower() == session["user"].lower():
                categories = mongo.db.categories.find().sort("category_name", 1)
                return render_template(
                    "edit_method.html", method=method, categories=categories)
            else:
                flash("You must be a method's creator to edit it")
                return redirect(url_for('get_methods'))
    except:
        flash("That method does not exist.")
        return redirect(url_for('get_methods'))


# The following function checks if the user has admin priveledges,
# the functions that follow it all use this check to grant said
# admin priledges.

def is_admin():
    if not session:
        return False
    if session['user'] == os.environ.get('ADMIN_ONE'):
        return True
    if session['user'] == os.environ.get('ADMIN_TWO'):
        return True
    return False


@app.route("/method/<method_id>/delete")
def delete_method(method_id):
    method = mongo.db.methods.find_one({"_id": ObjectId(method_id)})
    if session:
        is_user_admin = is_admin()
        if (method["created_by"].lower() == session["user"].lower()
                or is_user_admin):
            mongo.db.methods.remove({"_id": ObjectId(method_id)})
            flash("Method Successfully Deleted")
            return redirect(url_for("get_methods"))
        else:
            flash("You must be a method's creator to delete it")
            return redirect(url_for('get_methods'))
    else:
        flash("You must be a method's creator to delete it")
        return redirect(url_for('get_methods'))


@app.route("/category/add", methods=["GET", "POST"])
def add_category():
    is_user_admin = is_admin()
    if not is_user_admin:
        flash("You must be an administrator to view that page")
        return redirect(url_for('get_methods'))
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for('profile', username=session['user']))

    return render_template("add_category.html")


@app.route("/category/<category_id>/edit", methods=["GET", "POST"])
def edit_category(category_id):
    is_user_admin = is_admin()
    if not is_user_admin:
        flash("You must be an administrator to view that page")
        return redirect(url_for('get_methods'))
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for('profile', username=session['user']))

    try:
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category)
    except:
        flash('That category does not exist')
        return redirect(url_for("get_methods"))


@app.route("/category/<category_id>/delete")
def delete_category(category_id):
    is_user_admin = is_admin()
    if not is_user_admin:
        flash("You must be an administrator to do that")
        return redirect(url_for('get_methods'))
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for('profile', username=session['user']))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
