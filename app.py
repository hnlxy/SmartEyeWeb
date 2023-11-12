from flask import render_template, Flask, session, redirect, request, jsonify
from factory import create_app

app = create_app()


@app.route('/index/<username>')
def index(username):
    if session.get(username) == username:
        return render_template('index.html')
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
