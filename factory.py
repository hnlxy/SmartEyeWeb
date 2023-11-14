from flask import Flask
from os import urandom
from extensions import init_app
import settings
from blueprints.user import user_bp
from blueprints.elderly import elderly_bp
from blueprints.nurse import nurse_bp
from blueprints.permission import permission_bp
from blueprints.cost import cost_bp
from blueprints.system_report import system_report_bp
from blueprints.account import account_bp
from blueprints.system_setting import setting_bp
from extensions import login_manager


def create_app():
    app = Flask(__name__)

    # TODO 加载配置
    app.config.from_object(settings.DevelopmentConfig)
    login_manager.init_app(app)
    init_app(app)
    # TODO 注册蓝本
    app.register_blueprint(user_bp)
    app.register_blueprint(elderly_bp)
    app.register_blueprint(nurse_bp)
    app.register_blueprint(permission_bp)
    app.register_blueprint(cost_bp)
    app.register_blueprint(system_report_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(setting_bp)
    app.secret_key = urandom(66)
    # TODO 初始化配置
    # db.init_app(app)

    return app
