from . import elderly_bp
from flask import Flask, render_template


@elderly_bp.route('/pages/elderly-management/elderly-member')
def elderly_member():
    results = [
        ("#A-122014","张三","26 Jan 2021","casdasd","三级","病危","614"),
        ("#A-122015","李四","27 Jan 2021","苏打水","二级","健康","684"),
        ("#A-122016","王五","28 Jan 2021","噶啥的","一级","恢复","782"),
        ("#A-122017","李六","28 Jan 2021","佛山市","十级","病危","614"),
    ]
    return render_template('pages/elderly-management/elderly-member.html', results=results)