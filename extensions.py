from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, current_user, LoginManager, UserMixin


class User(UserMixin):
    def __init__(self, username):
        self.id = username
        

login_manager = LoginManager()
login_manager.login_view = 'user.login'


@login_manager.user_loader
def load_user(user):
    return User(user)

# TODO 数据库
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
