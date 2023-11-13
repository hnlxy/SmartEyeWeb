from . import elderly_bp
from flask import Flask, render_template
from flask_login import login_required


@elderly_bp.route('/pages/elderly-management/elderly-rights')
@login_required
def elderly_rights():
    return render_template('pages/elderly-management/elderly-rights.html')