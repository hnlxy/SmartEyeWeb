from flask import render_template
from flask_login import login_required
from blueprints.system_report import system_report_bp


@system_report_bp.route('/pages/system-report/system-report')
@login_required
def system_report():
    return render_template('pages/system-report/system_report.html')
