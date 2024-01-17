from . import nurse_bp
from flask import Flask, render_template, jsonify, request
from flask_login import login_required
from models import Caregiver


@nurse_bp.route('/nurse-information')
@login_required
def nurse_information():
    info = Caregiver.query.first()
    # print(info)
    if info:
        return render_template('pages/nurse-management/nurse_information.html',
                               id_name=info.caregiver_id + '-' + info.caregiver_name,
                               experience=info.experience,
                               skills=info.skills,
                               contact=f'电话：{info.caregiver_phone}<br>邮箱：{info.caregiver_email}',
                               image=f'/{info.profile_photo}')
    else:
        return render_template('pages/nurse-management/nurse_information.html',
                               id_name='N/A',
                               experience='N/A',
                               skills='N/A',
                               contact='N/A',
                               image='/static/assets/images/faces/face1.jpg')


@nurse_bp.route('/get_elderly', methods=['POST'])
@login_required
def get_elderly():
    data = request.get_json()
    id = data['id']
    name = data['name']
    care_elderly = [
        {'name': '王奶奶', 'room': '201'},
        {'name': '刘奶奶', 'room': '202'},
        {'name': '李奶奶', 'room': '203'},
        {'name': '陈奶奶', 'room': '204'},
        {'name': '张奶奶', 'room': '205'},
        {'name': '赵奶奶', 'room': '206'},
        {'name': '孙奶奶', 'room': '207'},
        {'name': '周奶奶', 'room': '208'},
        {'name': '钱奶奶', 'room': '209'},
        {'name': '吴奶奶', 'room': '210'},
    ]
    return jsonify({'success': True, 'message': '获取成功', 'care_elderly': care_elderly}), 200, {
        'ContentType': 'application/json'}


@nurse_bp.route('/get_nurses', methods=['POST'])
@login_required
def get_nurse():
    info = Caregiver.query.all()
    nurses = []
    for i in info:
        item = {'id_name': i.caregiver_id + '-' + i.caregiver_name, 'experience': i.experience, 'skills': i.skills,
                'contact': f'电话：{i.caregiver_phone}\n邮箱：{i.caregiver_email}', 'image': f'/{i.profile_photo}'}
        nurses.append(item)
    # nurses = [
    #     {
    #         'id_name': '001-张三',
    #         'experience': '拥有多年的护理经验。',
    #         'skills': '具备广泛的护理技能，包括日常生活协助、药物管理、身体活动支持以及应对紧急情况的能力。',
    #         'contact': '电话：12345678910\n邮箱：smarteye@smarteye.com',
    #         'image': '/static/assets/images/faces/face1.jpg'
    #     },
    #     {
    #         'id_name': '002-李四',
    #         'experience': '曾在几家知名养老院工作过。',
    #         'skills': '为每位老年人创造一个温馨、舒适和尊严的环境，让他们感到被尊重和重视。始终以微笑和关怀的态度对待每一位老年人，帮助他们度过每一天。',
    #         'contact': '电话：12345678910\n邮箱：smarteye@smarteye.com',
    #         'image': '/static/assets/images/faces/face2.jpg'
    #     },
    #     {
    #         'id_name': '003-王五',
    #         'experience': '曾在不同类型的养老院工作。',
    #         'skills': '善于与老年人建立亲密的关系，倾听他们的需求并提供温暖和支持。',
    #         'contact': '电话：12345678910\n邮箱：smarteye@smarteye.com',
    #         'image': '/static/assets/images/faces/face3.jpg'
    #     }
    # ]
    return jsonify({'success': True, 'message': '获取成功', 'nurses': nurses}), 200, {'ContentType': 'application/json'}
