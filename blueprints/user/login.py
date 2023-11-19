from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, LoginManager, UserMixin
from extensions import User, db
from models import Admin, Announcement


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('pages/user/login.html')
    else:
        data = request.get_json()
        username = data['username']
        password = data['password']
        queried_result = db.session.query(Admin).filter(Admin.username == username).all()

        # 查询到0条记录
        if len(queried_result) == 0:
            return jsonify({'success': False, 'message': '此账户未注册'}), 200, {'ContentType': 'application/json'}
        # username字段加了unique约束
        elif len(queried_result) > 1:
            return jsonify({'success': False, 'message': '登陆失败'}), 200, {'ContentType': 'application/json'}
        # 账户和密码均正确
        elif queried_result[0].username == username and queried_result[0].password == password:
            user = User(username)
            login_user(user)
            return redirect('/index')
        # 查询到账户，但密码错误
        else:
            return jsonify({'success': False, 'message': '密码错误'}), 200, {'ContentType': 'application/json'}
