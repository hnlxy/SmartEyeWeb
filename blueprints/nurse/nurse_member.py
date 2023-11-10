from . import nurse_bp
from flask import Flask, render_template


@nurse_bp.route('/pages/nursing-management/nurse-member')
def nurse_member():
    return render_template('pages/nursing-management/nurse-member.html')