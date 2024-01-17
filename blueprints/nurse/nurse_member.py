from . import nurse_bp
from flask import Flask, render_template, request, jsonify
from flask_login import login_required
from models import Caregiver
from extensions import db
import os


def delete_picture(nurse_id, nurse_name):
    # 定义可能的图片扩展名列表
    possible_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    deleted = False
    # 构建不带扩展名的文件名
    base_file_name = f"{nurse_id}{nurse_name}"
    # 创建文件路径的基本部分
    for folder in ['profile_picture', 'cover_picture']:
        base_path = os.path.join('static', 'assets', 'images', 'nurse', folder)
        # 检查每种可能的扩展名
        for ext in possible_extensions:
            file_path = os.path.join(base_path, base_file_name + ext)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    deleted = True
                except Exception as e:
                    print(f"Error while deleting file: {e}")
                    return False
    if not deleted:
        print("文件没找到。")
    return deleted


@nurse_bp.route('/nurse-member')
@login_required
def nurse_member():
    page = request.args.get('page', default=1, type=int)
    results = []
    info = Caregiver.query.all()
    for i in info:
        temp = [i.caregiver_id, i.caregiver_name, i.caregiver_age, i.caregiver_gender, i.caregiver_department,
                i.caregiver_phone, i.caregiver_address]
        results.append(temp)
    total = len(info) // 12 + 1
    return render_template('pages/nurse-management/nurse_member.html', results=results, page=page, total=total)


@nurse_bp.route('/delete_nurse', methods=['POST'])
@login_required
def delete_nurse():
    data = request.get_json()
    ids = data['id']
    for i in ids:
        info = Caregiver.query.filter(Caregiver.caregiver_id == i.split('-')[0],
                                      Caregiver.caregiver_name == i.split('-')[
                                          1]).first()
        res = delete_picture(info.caregiver_id, info.caregiver_name)
        if res:
            db.session.delete(info)
        else:
            db.session.rollback()
            return jsonify({'success': False, 'message': '删除失败！'}), 200, {'ContentType': 'application/json'}
    db.session.commit()
    return jsonify({'success': True, 'message': '删除成功！'}), 200, {'ContentType': 'application/json'}
