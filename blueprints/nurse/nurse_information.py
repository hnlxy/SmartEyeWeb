from . import nurse_bp
from flask import Flask, render_template
from flask_login import login_required


@nurse_bp.route('/pages/nursing-management/nurse-information')
@login_required
def nurse_information():
    return render_template('pages/nurse-management/nurse_information.html')
