from . import elderly_bp
from flask import Flask, render_template


@elderly_bp.route('/pages/elderly-management/elderly-member')
def elderly_member():
    return render_template('pages/elderly-management/elderly-member.html')
