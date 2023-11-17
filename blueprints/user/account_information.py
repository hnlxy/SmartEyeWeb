from flask import render_template
from flask_login import login_required
from blueprints.user import user_bp


@user_bp.route('/pages/user/account-information')
@login_required
def account_information():
    return render_template('pages/user/account_information.html')
