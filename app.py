from flask import render_template,Flask

from factory import create_app

app = create_app()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
