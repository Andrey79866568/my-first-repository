from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)
params = dict()
params['title'] = 'Заготовка'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base_nav.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params['name'] = prof
    return render_template('tren.html', **params)


@app.route('/list_prof/<type_of_list>')
def list_view(type_of_list):
    return render_template('list_prof.html', type=type_of_list)


@app.route('/answer')
def answer():
    params['title'] = 'Анкета-ответ'
    params['surname'] = 'Watny'
    params['name'] = 'Mark'
    params['education'] = 'выше среднего'
    params['profession'] = 'Штурман марсохода'
    params['sex'] = 'male'
    params['motivation'] = 'Всегда мечтал застрять на Марсе!'
    params['ready'] = True
    return render_template('avto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
