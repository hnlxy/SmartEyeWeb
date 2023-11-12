from flask import render_template

from blueprints.account import account_bp


@account_bp.route('/pages/account/account-information')
def account_information():
    return render_template('pages/account/account_information.html')
