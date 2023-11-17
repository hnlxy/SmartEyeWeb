from flask import render_template
from flask_login import login_required
from blueprints.system_setting import setting_bp


@setting_bp.route('/setting-information')
@login_required
def system_setting():
    return render_template('pages/system-setting/setting_information.html')
