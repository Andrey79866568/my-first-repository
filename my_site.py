from flask import Flask, make_response, url_for, jsonify, request, render_template, redirect, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from sqlalch_data.data.db_session import *
from sqlalch_data.data.__all_models import *
import jobs_api
import json
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '#Mars$%Colonisation$%Secret$%Key!!!'
params = dict()
params['title'] = 'Our Mission'
params['profession'] = 'anonymous'
params['sex'] = 'male'
params['oldest'] = 20
params['style'] = '/static/css/style.css'

app.register_blueprint(jobs_api.blueprint)

global_init('sqlalch_data/db/mars.db')
db_sess = create_session()

login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
                               form=form, **params)
    return render_template('login_for_avtor.html', form=form, **params)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = AddJob()
    if form.validate_on_submit():
        job = Jobs()

        category = db_sess.query(Category).filter(Category.id == form.category.data).first()
        if category:
            job.category = category
        else:
            abort(500)

        job.job = form.job.data
        if form.team_leader.data == -1:
            job.team_leader = current_user.id
        else:
            job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        db_sess.merge(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job_shab.html', form=form, **params)


@app.route('/add_depart', methods=['GET', 'POST'])
@login_required
def add_depart():
    form = AddDepartament()
    if form.validate_on_submit():
        depo = Departament()
        depo.title = form.title.data
        depo.chief = form.chief.data
        for member in map(int, form.members.data.split(',')):
            depo.members.append(db_sess.query(User).filter(User.id == member).first())
        depo.email = form.email.data
        db_sess.merge(depo)
        db_sess.commit()
        return redirect('/departs')
    return render_template('add_depo_shab.html', form=form, **params)


@app.route('/depart_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_depart(id):
    form = AddDepartament()
    if request.method == "GET":
        depart = db_sess.query(Departament).filter(Departament.id == id).first()
        if depart:
            form.title.data = depart.title
            form.chief.data = depart.chief
            form.members.data = str(depart.members)[1:-1]
            form.email.data = depart.email
        else:
            abort(404)
    if form.validate_on_submit():
        depart = db_sess.query(Departament).filter(Departament.id == id).first()
        if depart:
            depart.title = form.title.data
            depart.chief = form.chief.data

            depart.members = []
            for member in map(int, form.members.data.split(',')):
                depart.members.append(db_sess.query(User).filter(User.id == member).first())

            depart.email = form.email.data
            db_sess.commit()
            return redirect('/departs')
        else:
            abort(404)
    return render_template('add_depo_shab.html', form=form, **params)


@app.route('/depart_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def depart_delete(id):
    depart = db_sess.query(Departament).filter(Departament.id == id).first()
    if depart:
        db_sess.delete(depart)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departs')


@app.route('/jobs_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = AddJob()
    if request.method == "GET":
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            form.job.data = jobs.job
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.category.data = jobs.category.id
        else:
            abort(404)
    if form.validate_on_submit():
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            category = db_sess.query(Category).filter(Category.id == form.category.data).first()
            if category:
                jobs.category = category
            else:
                abort(500)
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job_shab.html', form=form, **params)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


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


@app.route('/')
@app.route('/index')
def index():
    return render_template('magazine.html', works=db_sess.query(Jobs).order_by(Jobs.collaborators.asc()),
                           **params)


@app.route('/departs')
def index_dep():
    return render_template('magazine_dep.html',
                           departs=db_sess.query(Departament).order_by(Departament.chief.asc()), **params)


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


@app.route('/table/<sex>/<oldest>')
def design(sex, oldest):
    params['sex'] = sex
    params['oldest'] = oldest
    return render_template('table.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
