from . import nurse_bp
from flask import Flask, render_template, jsonify, request
from flask_login import login_required
from datetime import datetime
from models import Caregiver, CaregiverTasks
from extensions import db


def parse_time(time_str):
    """将时间字符串转换为 datetime 对象"""
    date_str, time_range = time_str.split(' ')
    start_time_str, end_time_str = time_range.split('-')
    start_datetime = datetime.strptime(date_str + ' ' + start_time_str, '%Y-%m-%d %H:%M')
    end_datetime = datetime.strptime(date_str + ' ' + end_time_str, '%Y-%m-%d %H:%M')
    return start_datetime, end_datetime


def is_overlap(time_str1, time_str2):
    """判断两个时间段是否有交叉"""
    start1, end1 = parse_time(time_str1)
    start2, end2 = parse_time(time_str2)

    return max(start1, start2) < min(end1, end2)


# 测试
time1 = '2023-11-21 08:03-08:10'
time2 = '2023-11-21 08:05-08:15'


# print(is_overlap(time1, time2))  # 应该返回 True，因为时间段有交叉
@nurse_bp.route('/task-arrangement')
@login_required
def task_arrangement():
    nurse_name = []
    info = Caregiver.query.all()
    for i in info:
        nurse_name.append(i.caregiver_id + '-' + i.caregiver_name)
    return render_template('pages/nurse-management/task_arrangement.html', nurses=nurse_name)


@nurse_bp.route('/get_tasks', methods=['POST'])
@login_required
def get_tasks():
    data = request.get_json()
    id = data['id']
    name = data['name']
    tasks = [
        {'name': '任务1', 'date': '2024-01-21 08:03-08:10', 'status': '未完成'},
        {'name': '任务2', 'date': '2024-01-22 10:20-12:00', 'status': '未完成'},
        {'name': '任务3', 'date': '2024-01-28 15:00-17:00', 'status': '已完成'},
        {'name': '任务4', 'date': '2024-01-21 08:20-08:40', 'status': '已完成'}
    ]

    return jsonify({'success': True, 'message': '获取成功', 'tasks': tasks}), 200, {'ContentType': 'application/json'}


@nurse_bp.route('/add_task', methods=['POST'])
@login_required
def add_task():
    data = request.get_json()
    id = data['id']
    name = data['name']
    task = data['task']
    date = data['date']
    res = CaregiverTasks.query.filter(CaregiverTasks.task_date >= date).all()
    for i in res:
        if is_overlap(date, i.task_date):
            return jsonify({'success': False, 'message': '时间段有交叉'}), 200, {'ContentType': 'application/json'}
    new_task = CaregiverTasks(
        caregiver_id=id,
        caregiver_name=name,
        task=task,
        task_date=date,
        task_status='未完成'
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'success': True, 'message': '添加成功'}), 200, {'ContentType': 'application/json'}


@nurse_bp.route('/delete_task', methods=['POST'])
@login_required
def delete_task():
    data = request.get_json()
    id = data['id']
    name = data['name']
    task = data['task']
    date = data['date']
    return jsonify({'success': True, 'message': '删除成功'}), 200, {'ContentType': 'application/json'}
