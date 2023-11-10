from . import nurse_bp
from flask import Flask, render_template


@nurse_bp.route('/pages/nursing-management/task-arrangement')
def task_arrangement():
    return render_template('pages/nursing-management/task-arrangement.html')
