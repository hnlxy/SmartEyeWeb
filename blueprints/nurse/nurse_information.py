from . import nurse_bp
from flask import Flask, render_template


@nurse_bp.route('/pages/nursing-management/nurse-information')
def nurse_information():
    return render_template('pages/nursing-management/nurse-information.html')
