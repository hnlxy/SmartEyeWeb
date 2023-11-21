from . import nurse_bp
from flask import Flask, render_template, jsonify, request
from flask_login import login_required
from datetime import datetime


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
    nurse_name = ['001-张三', '002-李四', '003-王五']
    return render_template('pages/nurse-management/task_arrangement.html', nurses=nurse_name)


@nurse_bp.route('/get_tasks', methods=['POST'])
@login_required
def get_tasks():
    tasks = [
        {'name': '任务1', 'date': '2023-11-21 08:03-08:10', 'status': '未完成'},
        {'name': '任务2', 'date': '2023-11-22 10:20-12:00', 'status': '未完成'},
        {'name': '任务3', 'date': '2023-11-28 15:00-17:00', 'status': '已完成'},
        {'name': '任务4', 'date': '2023-11-21 08:20-08:40', 'status': '已完成'}
    ]
    return jsonify({'success': True, 'message': '获取成功', 'tasks': tasks}), 200, {'ContentType': 'application/json'}


@nurse_bp.route('/add_task', methods=['POST'])
@login_required
def add_task():
    data = request.get_json()
    return jsonify({'success': True, 'message': '添加成功'}), 200, {'ContentType': 'application/json'}


@nurse_bp.route('/delete_task', methods=['POST'])
@login_required
def delete_task():
    data = request.get_json()
    return jsonify({'success': True, 'message': '删除成功'}), 200, {'ContentType': 'application/json'}
