from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '#Mars$%Colonisation$%Secret$%Key!!!'
params = dict()
params['title'] = 'Our Mission'
params['profession'] = 'anonymous'
params['style'] = '/static/css/style.css'
params_answer = dict()
params_answer['style'] = '/static/css/style.css'


class AlertForm(FlaskForm):
    user1 = StringField('Логин', validators=[DataRequired()])
    password1 = PasswordField('Пароль', validators=[DataRequired()])
    user2 = StringField('Логин', validators=[DataRequired()])
    password2 = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('СТАРТ')


@app.route('/login', methods=['GET', 'POST'])
def login_astr():
    if request.method == 'GET':
        return render_template('login_astr.html')
    elif request.method == 'POST':
        params_answer['title'] = 'Анкета-ответ'
        params_answer['surname'] = request.form['surname']
        params_answer['name'] = request.form['name']
        params_answer['education'] = request.form['class']
        params_answer['profession'] = request.form['profs']
        params_answer['sex'] = request.form['sex']
        params_answer['motivation'] = request.form['about']
        if 'accept_to_stay' in request.form:
            params_answer['ready'] = request.form['accept_to_stay']
        else:
            params_answer['ready'] = 'off'
        params['profession'] = params_answer['profession']
        return answer()


@app.route('/')
@app.route('/index')
def index():
    return render_template('base_nav.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params['name_prof'] = prof
    return render_template('tren.html', **params)


@app.route('/list_prof/<type_of_list>')
def list_view(type_of_list):
    params['type'] = type_of_list
    return render_template('list_prof.html', **params)


@app.route('/answer')
def answer():
    return render_template('avto_answer.html', **params_answer)


# @app.route('/login_p', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)


@app.route('/alert')
def alert():
    if request.method == 'GET':
        params_alert = params.copy()
        params_alert['style'] = '/static/css/alert_style.css'
        form = AlertForm()
        if form.validate_on_submit():
            return redirect('/success')
        return render_template('alert.html', form=form, **params_alert)
    elif request.method == 'POST':
        print(request.form)
        return 'Тревога успешно объявлена'


@app.route('/distribution')
def distribution():
    list_rasp = ['Какой-то член экипажа', 'Какой-то член экипажа 1', 'Какой-то член экипажа 2',
                 'Какой-то член экипажа 3', 'Какой-то член экипажа 4']
    return render_template('distribution.html', list_rasp=list_rasp, **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
