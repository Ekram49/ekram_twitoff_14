# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db, Tweet, Users, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users.json")
def list_users():
    users_records = Users.query.all()
    print(users_records)
    users = parse_records(users_records)
    return jsonify(users)

@twitter_routes.route("/users")
def list_users_for_humans():
    
    users_records = Users.query.all()
    print(users_records)

    return render_template("users.html", message="Here's some books", users=users_records)

@twitter_routes.route("/users/new")
def new_users():
    return render_template("new_users.html")

@twitter_routes.route("/users/create", methods=["POST"])
def create_users():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    new_users = Users(users=request.form["users_name"])
    db.session.add(new_users)
    db.session.commit()

    return redirect("/users")
   