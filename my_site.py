from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    params = dict()
    params['title'] = 'Заготовка'
    return render_template('base_nav.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = dict()
    params['name'] = prof
    params['title'] = 'Заготовка'
    return render_template('tren.html', **params)


@app.route('/list_prof/<type_of_list>')
def list_view(type_of_list):
    return render_template('list_prof.html', type=type_of_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
