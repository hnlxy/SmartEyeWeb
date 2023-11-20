from flask import Blueprint

elderly_bp = Blueprint("elderly", __name__)

from . import elderly_rights
from . import elderly_member
from . import add_elderly

