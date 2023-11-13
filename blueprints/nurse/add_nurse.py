from . import nurse_bp
from flask import Flask, render_template
from flask_login import login_required


@nurse_bp.route('/pages/nursing-management/add-nurse')
@login_required
def add_nurse():
    return render_template('pages/nursing-management/add-nurse.html')
