from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
import json


@user_bp.route('/', methods=['GET'])
@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('/pages/account/login.html')
    else:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username == 'smarteye' and password == '123456':
            session[username] = username
            return redirect(f'/index/{username}')
        else:
            return jsonify({'success': False, 'message': '用户名或密码错误'}), 200, {'ContentType': 'application/json'}

