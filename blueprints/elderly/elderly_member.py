from . import elderly_bp
from flask import Flask, render_template
from flask_login import login_required


@elderly_bp.route('/elderly-member')
@login_required
def elderly_member():
    results = [
        ("#A-122014","李奶奶","26 Jan 2021","保定市","三级","病危","王芳","614"),
        ("#A-122015","王奶奶","27 Jan 2021","保定市","二级","健康","李丽","684"),
        ("#A-122016","赵爷爷","28 Jan 2021","保定市","一级","恢复","赵叶","782"),
        ("#A-122017","王爷爷","25 Jan 2021","保定市","二级","病危","李芬","614"),
        ("#A-122017","杨奶奶","17 Jan 2021","保定市","一级","健康","丁雨","612"),
        ("#A-122017","高爷爷","28 Jan 2021","保定市","二级","恢复","田浩","454"),
        ("#A-122017","丁奶奶","13 Jan 2021","保定市","一级","健康","李炮","664"),
        ("#A-122017","张爷爷","08 Jan 2021","保定市","二级","病危","钱大本","784"),
        
    ]
    return render_template('pages/elderly-management/elderly_member.html', results=results)