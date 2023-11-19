import json
from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from extensions import db
from models import *


@user_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('pages/admin/register.html')
    else:
        try:
            data = request.get_json()
            # print(data)
            admin = Admin(
                username=data["username"],
                password=data["password"],
                email=data["email"]
            )
            db.session.add(admin)
            db.session.commit()
            return jsonify({'success': True, 'message': '注册成功'}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            return jsonify({'success': False, 'message': '注册失败'}), 200, {'ContentType': 'application/json'}
