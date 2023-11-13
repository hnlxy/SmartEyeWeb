from flask import render_template, Flask, session, redirect, request, jsonify
from factory import create_app
from flask_login import LoginManager, login_required

app = create_app()


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
