from flask import render_template, request
from flask_login import login_required
from blueprints.system_report import system_report_bp


@system_report_bp.route('/system-report')
@login_required
def system_report():
    page = request.args.get('page', default=1, type=int)
    results = [
        ['000001', '2023-01-01 00:00:00', '新增长者', '张三', '正常', '院长'],
        ['000002', '2023-01-01 00:00:00', '新增护工', '小红', '正常', '院长'],
        ['000003', '2023-01-01 00:00:00', '#A-122014交接', '护工1&护工2', '异常', ''],
        ['000004', '2023-01-02 08:30:00', '设备维护', '李四', '异常', ''],
        ['000005', '2023-01-02 09:15:00', '健康检查', '王五', '正常', '护工3'],
        ['000006', '2023-01-02 10:00:00', '紧急救援', '赵六', '正常', '医护人员'],
        ['000007', '2023-01-03 11:20:00', '日常巡视', '孙七', '正常', '安保'],
        ['00008', '2023-01-03 16:00:00', '环境卫生', '郑十', '异常', '']
    ]
    total = 5
    return render_template('pages/system-report/system_report.html', results=results, page=page, total=total)
