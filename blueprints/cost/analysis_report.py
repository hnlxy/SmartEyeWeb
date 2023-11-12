from flask import render_template

from blueprints.cost import cost_bp


@cost_bp.route('/pages/cost-management/analysis-report')
def analysis_report():
    return render_template('pages/cost-management/analysis-report.html')
