from . import nurse_bp
from flask import Flask, render_template


@nurse_bp.route('/pages/nursing-management/add-nurse')
def add_nurse():
    return render_template('pages/nursing-management/add-nurse.html')
