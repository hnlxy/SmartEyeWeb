from flask import Blueprint

user_bp = Blueprint("user", __name__)

from . import login
from . import register
from . import account_information
