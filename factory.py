from flask import Flask
from sqlalchemy import text
from os import urandom
from extensions import db
import settings
from blueprints.user import user_bp
from blueprints.elderly import elderly_bp
from blueprints.nurse import nurse_bp
from blueprints.permission import permission_bp
from blueprints.cost import cost_bp
from blueprints.system_report import system_report_bp
from blueprints.system_setting import setting_bp
from extensions import login_manager


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")

    # TODO 加载配置
    app.config.from_object(settings.DevelopmentConfig)
    # TODO 注册蓝本
    app.register_blueprint(user_bp)
    app.register_blueprint(elderly_bp, url_prefix="/elderly-management")
    app.register_blueprint(nurse_bp, url_prefix="/nurse-management")
    app.register_blueprint(permission_bp, url_prefix="/permission-management")
    app.register_blueprint(cost_bp, url_prefix="/cost-management")
    app.register_blueprint(system_report_bp, url_prefix="/system-report")
    app.register_blueprint(setting_bp, url_prefix="/system-setting")
    app.secret_key = urandom(66)
    # TODO 初始化配置
    login_manager.init_app(app)
    db.init_app(app)

    return app
