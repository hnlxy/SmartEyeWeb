from flask import render_template
from flask_login import login_required
from blueprints.permission import permission_bp


@permission_bp.route('/child-permission')
@login_required
def child_permission():
    return render_template('pages/permission-management/child_permission.html')