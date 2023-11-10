from . import elderly_bp
from flask import Flask, render_template


@elderly_bp.route('/pages/elderly-management/elderly-rights')
def elderly_rights():
    return render_template('pages/elderly-management/elderly-rights.html')