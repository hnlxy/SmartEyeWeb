from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from extensions import db
from models import *


@user_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('pages/user/register.html')
    else:
        print("Hello")
        # data = request.get_json()
        # print(data)
        data = request.get_json()
        print(data)
        print(data is None)
        # admin = Admin(
        #     username=data["username"],
        #     password=data["password"],
        #     email=data["email"]
        # )
        # db.session.add(admin)
        # db.session.commit()
        return redirect("/login")
