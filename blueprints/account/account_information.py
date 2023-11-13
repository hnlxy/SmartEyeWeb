from flask import render_template
from flask_login import login_required
from blueprints.account import account_bp


@account_bp.route('/pages/account/account-information')
@login_required
def account_information():
    return render_template('pages/account/account_information.html')
