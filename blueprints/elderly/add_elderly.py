from . import elderly_bp
from flask import Flask, render_template
from flask_login import login_required


@elderly_bp.route('/pages/elderly-management/add-elderly')
@login_required
def add_elderly():
    return render_template('pages/elderly-management/add-elderly.html')
