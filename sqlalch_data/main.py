# from flask import Flask
# from data.db_session import *
# from data.__all_models import *
# import datetime
# #
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

name = input()
global_init(name)
db_sess = create_session()

users = db_sess.query(User).filter(User.address.like("module_1"), User.age < 21)
for i in users:
    i.address = "module_3"
db_sess.commit()

# app.run()
