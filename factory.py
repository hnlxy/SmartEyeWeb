from flask import Flask

import settings
from blueprints.user import user_bp
from blueprints.elderly import elderly_bp
from blueprints.nurse import nurse_bp
# from extensions import db


def create_app():
    app = Flask(__name__)
    # TODO ��������
    app.config.from_object(settings.DevelopmentConfig)
    # TODO ע������
    app.register_blueprint(user_bp)
    app.register_blueprint(elderly_bp)
    app.register_blueprint(nurse_bp)
    # TODO ��ʼ������
    # db.init_app(app)

    return app
