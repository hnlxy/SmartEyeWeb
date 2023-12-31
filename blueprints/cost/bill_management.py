from flask import render_template
from flask_login import login_required
from blueprints.cost import cost_bp


@cost_bp.route('/bill-management')
@login_required
def bill_management():
    return render_template('pages/cost-management/bill_management.html')
