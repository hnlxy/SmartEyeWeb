from flask import render_template

from blueprints.system_setting import setting_bp


@setting_bp.route('/pages/system-setting/setting-information')
def system_setting():
    return render_template('pages/system-setting/setting_information.html')
