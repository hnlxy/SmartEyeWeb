from flask import Blueprint

system_report_bp = Blueprint('system_report', __name__)

from . import system_report
