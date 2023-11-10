from . import elderly_bp
from flask import Flask, render_template


@elderly_bp.route('/pages/elderly-management/add-elderly')
def add_elderly():
    return render_template('pages/elderly-management/add-elderly.html')
