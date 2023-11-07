from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/pages/ui-features/buttons')
def pages_ui_features_buttons():
    return render_template('pages/ui-features/buttons.html')


if __name__ == '__main__':
    app.run()
