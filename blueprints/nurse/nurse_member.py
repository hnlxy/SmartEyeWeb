from . import nurse_bp
from flask import Flask, render_template, request, jsonify
from flask_login import login_required


@nurse_bp.route('/nurse-member')
@login_required
def nurse_member():
    page = request.args.get('page', default=1, type=int)
    results = [
        ("#A-122014", "ABCD", "35", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122015", "BCDA", "54", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122016", "TADS", "47", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122017", "AVCD", "53", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122014", "ABCD", "35", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122015", "BCDA", "54", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122016", "TADS", "47", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122017", "AVCD", "53", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122014", "ABCD", "35", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122015", "BCDA", "54", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122016", "TADS", "47", "男", "护理部", "12345678901", "保定市莲池区"),
        ("#A-122017", "AVCD", "53", "男", "护理部", "12345678901", "保定市莲池区"),
    ]
    total = 5
    return render_template('pages/nurse-management/nurse_member.html', results=results, page=page, total=total)


@nurse_bp.route('/delete_nurse', methods=['POST'])
@login_required
def delete_nurse():
    data = request.get_json()
    ids = data['id']
    return jsonify({'success': True, 'message': '删除成功！'}), 200, {'ContentType': 'application/json'}
