from flask import jsonify, Blueprint, request
from sqlalch_data.data.db_session import *
from sqlalch_data.data.__all_models import *
import datetime
from errors import *

blueprint = Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        db_sess = create_session()
        user = db_sess.query(User).get(user_id)
        if not user:
            raise NotFoundError('user')
        return jsonify(
            {'user': user.to_dict(only=('surname', 'name', 'age', 'position', 'speciality', 'address',
                                        'email', 'modified_date', 'city_from', 'departament_id'))}), 200
    except NotFoundError as error:
        return jsonify({'message': {'name': f'{str(error)} not found'}}), 404


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    try:
        if not request.json:
            return jsonify({'error': 'Empty request'}), 400
        elif not ('data' in request.json):
            return jsonify({'error': 'Bad request'}), 400
        data = request.json['data']
        db_sess = create_session()
        user: User = db_sess.query(User).get(user_id)
        if not user:
            raise NotFoundError('user')

        for key in data:
            if key in ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from']:
                exec(f'user.{key}=data[key]')
            if key == 'departament_id':
                departament = db_sess.query(Departament).filter(Departament.id == data['departament_id'])
                if not departament:
                    raise NotFoundError('departament')
                user.departament = departament
            if key == 'password':
                user.hashed_password = generate_password_hash(data['password'])
            else:
                if key in ['modified_date', 'id']:
                    return jsonify({'message': {'name': 'some of these properties cannot be changed'}}), 403
                return jsonify({'message': {'name': 'user have no this property'}}), 405

        user.modified_date = datetime.datetime.now()
        db_sess.commit()
        return jsonify({'message': {'success': 'ok'}}), 200
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'message': {'name': 'user with this email already exists'}}), 422
    except NotFoundError as error:
        return jsonify({'message': {'name': f'{str(error)} not found'}}), 404


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        db_sess = create_session()
        user = db_sess.query(User).get(user_id)
        if not user:
            raise NotFoundError('user')
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'message': {'success': 'ok'}}), 200
    except NotFoundError as error:
        return jsonify({'message': {'name': f'{str(error)} not found'}}), 404


@blueprint.route('/api/users', methods=['GET'])
def get_all():
    session = create_session()
    users = session.query(User).all()
    return jsonify({'users': [item.to_dict(
        only=('name', 'surname', 'age', 'email')) for item in users]}), 200


@blueprint.route('/api/users', methods=['POST'])
def post_user():
    try:
        if not request.json:
            return jsonify({'error': 'Empty request'}), 400
        elif not all(key in request.json for key in
                     ['surname', 'name', 'age', 'position', 'speciality',
                      'address', 'email', 'password', 'city_from', 'departament_id']):
            return jsonify({'error': 'Bad request'}), 400

        db_sess = create_session()
        user = User()
        user.surname = request.json['surname']
        user.name = request.json['name']
        user.age = request.json['age']
        user.position = request.json['position']
        user.speciality = request.json['speciality']
        user.address = request.json['address']
        user.email = request.json['email']
        user.password = request.json['password']
        user.city_from = request.json['city_from']
        departament = db_sess.query(Departament).filter(Departament.id == request.json['departament_id'])
        if not departament:
            raise NotFoundError('departament')
        user.departament = departament

        user.hashed_password = generate_password_hash(request.json['password'])
        user.modified_date = datetime.datetime.now()

        db_sess.add(user)
        db_sess.commit()
        return jsonify({'message': {'success': 'ok'}}), 200
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'message': {'name': 'user with this email already exists'}}), 422
