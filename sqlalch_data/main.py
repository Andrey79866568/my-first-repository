# from flask import Flask
# from data.db_session import *
# from data.__all_models import *
# import datetime


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

name = input()
global_init(name)
db_sess = create_session()
departament = db_sess.query(Department).filter(Department.id == 1).first()
list_ik = [int(i) for i in departament.members.split(', ')]
for i in list_ik:
    user = db_sess.query(User).filter(User.id == i).first()
    jobs = db_sess.query(Jobs).filter(Jobs.collaborators.like(f'%{user.id}%'))
    if sum([job.work_size for job in jobs]) >= 25:
        print(user.surname, user.name)

# db_sess.commit()
# app.run()
