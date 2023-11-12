from flask import Blueprint

setting_bp = Blueprint('setting', __name__)

from . import setting_information
