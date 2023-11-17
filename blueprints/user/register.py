from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for


@user_bp.route('/register')
def register():
    return render_template('pages/user/register.html')
