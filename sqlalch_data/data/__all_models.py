import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class AddJob(FlaskForm):
    team_leader = IntegerField('Лидер команды')
    job = TextAreaField("Содержание")
    work_size = IntegerField("На сколько работа в часах")
    collaborators = StringField("Поле для хранения id работников")
    category = IntegerField("Category")
    submit = SubmitField('Сделать')


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'categories'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)


association_table = sqlalchemy.Table(
    'association',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('news', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('news.id')),
    sqlalchemy.Column('category', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('category.id'))
)


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    categories = orm.relation("Category",
                              secondary="association",
                              backref="news")


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Позиция пользователя', validators=[DataRequired()])
    speciality = StringField('Специальность пользователя', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    city_from = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    departament_id = sqlalchemy.Column(sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey("departments.id"), nullable=True)
    departament = orm.relation('Departament')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f"{self.id}"


class Departament(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'departments'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    chief = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    members = orm.relation("User", back_populates='departament')
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)


class AddDepartament(FlaskForm):
    title = StringField("Название департамента")
    chief = IntegerField('Лидер')
    members = TextAreaField("Тут надо записать через запятую id рабочих")
    email = EmailField("Почта департамента")
    submit = SubmitField('Сделать')
