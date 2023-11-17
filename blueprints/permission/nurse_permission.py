from flask import render_template
from flask_login import login_required
from blueprints.permission import permission_bp


@permission_bp.route('/nurse-permission')
@login_required
def nurse_permission():
    return render_template('pages/permission-management/nurse_permission.html')