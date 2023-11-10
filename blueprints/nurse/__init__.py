from flask import Blueprint

nurse_bp = Blueprint("nurse", __name__)

from . import nurse_information
from . import nurse_member
from . import add_nurse
from . import task_arrangement
