from . import nurse_bp
from flask import Flask, render_template
from flask_login import login_required


@nurse_bp.route('/add-nurse')
@login_required
def add_nurse():
    return render_template('pages/nurse-management/add_nurse.html')
