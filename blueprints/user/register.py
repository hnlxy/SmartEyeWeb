from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for
from extensions import db
from models import *


@user_bp.route('/register', methods=["get", "post"])
def register():
    # print(request.form)
    if request.method == "GET":
        return render_template('pages/user/register.html')
    elif request.method == "POST":
        admin = Admin(
            username=request.form.get("username"),
            password=request.form.get("password"),
            email=request.form.get("email")
        )
        db.session.add(admin)
        db.session.commit()
        return redirect("/login")
