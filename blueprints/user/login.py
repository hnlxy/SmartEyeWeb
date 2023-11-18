from blueprints.user import user_bp
from flask import request, render_template, redirect, session, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, LoginManager, UserMixin
from extensions import User, db
from models import Announcement


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    # 测试数据库连接
    # result = db.session.query(Announcement).all()
    # print(result[0].title)
    # ann = Announcement(title="我", content="你好", publication_date="2022-01-01")
    # db.session.add(ann)
    # db.session.commit()

    if request.method == 'GET':
        return render_template('pages/user/login.html')
    else:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username == 'smarteye' and password == '123456':
            user = User(username)
            login_user(user)
            return redirect('/index')
        else:
            return jsonify({'success': False, 'message': '用户名或密码错误'}), 200, {'ContentType': 'application/json'}
