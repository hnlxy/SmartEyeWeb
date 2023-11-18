from . import elderly_bp
from flask import Flask, render_template
from flask_login import login_required


@elderly_bp.route('/add_guardian')
@login_required
def add_guardian():
    return render_template('pages/elderly-management/add_guardian.html')