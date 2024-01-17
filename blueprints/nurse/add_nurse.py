import datetime
from . import nurse_bp
from flask import Flask, render_template, request, jsonify
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from extensions import db
from models import Caregiver


def save_picture(file, nurse_id, nurse_name, sign):
    # 获取安全的文件名
    original_filename = secure_filename(file.filename)
    # 分离文件名和扩展名
    file_name, file_extension = os.path.splitext(original_filename)
    # 生成新的文件名，包含护士的 ID
    new_filename = f"{nurse_id}{nurse_name}{file_extension}"
    # 创建保存路径
    if sign == 'profile_picture':
        save_path = os.path.join('static', 'assets', 'images', 'nurse', 'profile_picture', new_filename)
    else:
        save_path = os.path.join('static', 'assets', 'images', 'nurse', 'cover_picture', new_filename)
    # 保存文件
    file.save(save_path)
    return save_path


@nurse_bp.route('/add-nurse', methods=['GET', 'POST'])
@login_required
def add_nurse():
    if request.method == 'GET':
        return render_template('pages/nurse-management/add_nurse.html')
    else:
        try:
            profile_picture = request.files['profile_picture']
            cover_picture = request.files['cover_picture']
            nurse_id = request.form['nurse_id']
            nurse_name = request.form['full_name']
            telephone = request.form['telephone']
            age = request.form['age']
            gender = request.form['gender']
            department = request.form['department']
            email = request.form['email']
            address = request.form['address']
            skills = request.form['skills']
            experience = request.form['experience']
            path1 = save_picture(profile_picture, nurse_id, nurse_name, 'profile_picture')
            path2 = save_picture(cover_picture, nurse_id, nurse_name, 'cover_picture')
            caregiver = Caregiver(
                caregiver_id=nurse_id,
                caregiver_name=nurse_name,
                caregiver_age=int(age),
                caregiver_phone=telephone,
                caregiver_address=address,
                hired_date=datetime.datetime.now().date(),
                caregiver_gender=gender,
                caregiver_email=email,
                caregiver_department=department,
                skills=skills,
                experience=experience,
                profile_photo='/' + path1,
                qualification_photo='/' + path2
            )
            db.session.add(caregiver)
            db.session.commit()
            return jsonify({'success': True, 'message': '添加成功'}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            print(e)
            return jsonify({'success': False, 'message': '添加失败'}), 200, {'ContentType': 'application/json'}
