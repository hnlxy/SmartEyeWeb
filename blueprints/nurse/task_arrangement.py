from . import nurse_bp
from flask import Flask, render_template
from flask_login import login_required


@nurse_bp.route('/pages/nursing-management/task-arrangement')
@login_required
def task_arrangement():
    return render_template('pages/nursing-management/task-arrangement.html')
