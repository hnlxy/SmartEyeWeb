from flask import render_template

from blueprints.permission import permission_bp


@permission_bp.route('/pages/permission-management/child-permission')
def child_permission():
    return render_template('pages/permission-management/child-permission.html')