from flask import Flask

import settings
from blueprints.user import user_bp
# from extensions import db


def create_app():
    app = Flask(__name__)
    # TODO º”‘ÿ≈‰÷√
    app.config.from_object(settings.DevelopmentConfig)
    # TODO ◊¢≤·¿∂±æ
    app.register_blueprint(user_bp)
    # TODO ≥ı ºªØ≈‰÷√
    # db.init_app(app)

    return app
