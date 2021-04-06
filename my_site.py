from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from sqlalch_data.data.db_session import *
from sqlalch_data.data.__all_models import *
import json
from flask_login import LoginManager, login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '#Mars$%Colonisation$%Secret$%Key!!!'
params = dict()
params['title'] = 'Our Mission'
params['profession'] = 'anonymous'
params['sex'] = 'male'
params['oldest'] = 20
params['style'] = '/static/css/style.css'
params_answer = dict()
params_answer['style'] = '/static/css/style.css'

global_init('sqlalch_data/db/mars.db')
db_sess = create_session()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login_for_avtor.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login_for_avtor.html', title='Авторизация', form=form)


class AlertForm(FlaskForm):
    user1 = StringField('Логин', validators=[DataRequired()])
    password1 = PasswordField('Пароль', validators=[DataRequired()])
    user2 = StringField('Логин', validators=[DataRequired()])
    password2 = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('СТАРТ')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register_form.html',
                                   form=form,
                                   message="Пароли не совпадают", **params)
        db_sess = create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register_form.html',
                                   form=form,
                                   message="Такой пользователь уже есть", **params)
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            hashed_password=generate_password_hash(form.password.data)
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register_form.html', form=form, **params)


@app.route('/login_dfdf', methods=['GET', 'POST'])
def login_astr():
    if request.method == 'GET':
        return render_template('login_astr.html')
    elif request.method == 'POST':
        params_answer['title'] = 'Анкета-ответ'
        params_answer['surname'] = request.form['surname']
        params_answer['name'] = request.form['name']
        params_answer['education'] = request.form['class']
        params_answer['profession'] = request.form['profs']
        params_answer['sex'] = params['sex'] = request.form['sex']
        params_answer['motivation'] = request.form['about']
        params_answer['oldest'] = params['oldest'] = request.form['oldest']
        if 'accept_to_stay' in request.form:
            params_answer['ready'] = request.form['accept_to_stay']
        else:
            params_answer['ready'] = 'off'
        params['profession'] = params_answer['profession']
        return answer()


@app.route('/')
@app.route('/index')
def index():
    return render_template('magazine.html', works=db_sess.query(Jobs).order_by(Jobs.collaborators.asc()),
                           **params)


@app.route('/training/<prof>')
def training(prof):
    return render_template('tren.html', name_prof=prof, **params)


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


@app.route('/table/<sex>/<oldest>')
def design(sex, oldest):
    params['sex'] = sex
    params['oldest'] = oldest
    return render_template('table.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
