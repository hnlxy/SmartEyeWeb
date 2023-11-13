from . import nurse_bp
from flask import Flask, render_template
from flask_login import login_required


@nurse_bp.route('/pages/nursing-management/nurse-member')
@login_required
def nurse_member():
    return render_template('pages/nursing-management/nurse-member.html')