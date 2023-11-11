from flask import Blueprint

permission_bp = Blueprint("permission", __name__)

from . import nurse_permission
from . import child_permission