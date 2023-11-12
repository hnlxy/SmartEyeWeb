from flask import render_template

from blueprints.cost import cost_bp


@cost_bp.route('/pages/cost-management/bill-management')
def bill_management():
    return render_template('pages/cost-management/bill-management.html')
