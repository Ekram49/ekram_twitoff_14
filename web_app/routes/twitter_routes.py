# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db, Tweet, User, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users.json")
def list_users():
    user_records = User.query.all()
    print(user_records)
    users = parse_records(user_records)
    return jsonify(users)

@twitter_routes.route("/users")
def list_users_for_humans():
    
    user_records = User.query.all()
    print(user_records)

    return render_template("users.html", message="Here's some books", users=user_records)

@twitter_routes.route("/users/new")
def new_user():
    return render_template("new_user.html")

@twitter_routes.route("/users/create", methods=["POST"])
def create_user():
    print("FORM DATA:", dict(request.form))

    user_new = User(title=request.form["user_name"])
    db.session.add(user_new)
    db.session.commit()

    return redirect("/users")
   