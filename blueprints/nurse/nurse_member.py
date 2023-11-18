from . import nurse_bp
from flask import Flask, render_template
from flask_login import login_required


@nurse_bp.route('/nurse-member')
@login_required
def nurse_member():
    results = [
        ("#A-122014", "ABCD", "35", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122015", "BCDA", "54", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122016", "TADS", "47", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122017", "AVCD", "53", "男", "护理部", "12345678901", "保定市莲池区"),
    ]
    return render_template('pages/nurse-management/nurse_member.html', results=results)