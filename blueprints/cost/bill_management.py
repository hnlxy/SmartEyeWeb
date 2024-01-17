from flask import render_template, request
from flask_login import login_required
from blueprints.cost import cost_bp


@cost_bp.route('/bill-management')
@login_required
def bill_management():
    page = request.args.get('page', default=1, type=int)
    results = [
        ['000001', '2023-01-01 00:00:00', '餐饮费', 500, '张三', '已交'],
        ['000002', '2023-01-01 00:00:00', '床位费', 800, '李四', '未交'],
        ['000003', '2023-01-01 00:00:00', '护理费', 1000, '王五', '已交'],
        ['000004', '2023-01-02 08:30:00', '餐饮费', 500, '赵六', '已交'],
        ['000005', '2023-01-02 09:15:00', '护理费', 1000, '孙七', '未交'],
        ['000006', '2023-01-02 10:00:00', '检查费', 2000, '王八', '未交'],
    ]
    total = 5
    return render_template('pages/cost-management/bill_management.html', results=results, page=page, total=total)
