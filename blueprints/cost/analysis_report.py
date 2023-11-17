from flask import render_template
from flask_login import login_required
from blueprints.cost import cost_bp


@cost_bp.route('/analysis-report')
@login_required
def analysis_report():
    return render_template('pages/cost-management/analysis_report.html')
