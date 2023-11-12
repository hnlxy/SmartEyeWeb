from flask import Blueprint

cost_bp = Blueprint('cost', __name__)

from . import analysis_report
from . import bill_management
