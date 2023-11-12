from flask import Blueprint

account_bp = Blueprint('account', __name__)

from . import account_information
