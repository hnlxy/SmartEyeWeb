from . import elderly_bp
from flask import Flask, render_template,request, jsonify
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from models import Elder  
from datetime import datetime


@elderly_bp.route('/elderly-member')
@login_required
def elderly_member():
    page = request.args.get('page', default=1, type=int)
    results = []
    info = Elder.query.all()
    for i in info:
        age = datetime.now().year - i.elder_birth.year
        temp = [i.elder_id, i.elder_name, i.elder_gender, i.elder_address,age,i.assigned_caregiver,
                i.care_level, i.room_number]
        results.append(temp)
    total = len(info) // 12 + 1
    return render_template('pages/elderly-management/elderly_member.html', results=results, page=page, total_pages=total)
