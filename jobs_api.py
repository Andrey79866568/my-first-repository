from flask import jsonify, Blueprint, request
from sqlalch_data.data.db_session import *
from sqlalch_data.data.__all_models import *
import datetime

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                    'is_finished', 'category_id'))
                    for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_news(jobs_id):
    db_sess = create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                'is_finished', 'category_id'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators',
                  'is_finished', 'category_id']):
        return jsonify({'error': 'Bad request'})
    db_sess = create_session()
    if db_sess.query(Jobs).get(request.json['id']):
        return jsonify({'errors': 'Id already exists'})
    job = Jobs()
    category = db_sess.query(Category).filter(Category.id == request.json['category_id']).first()
    if category:
        job.category = category
    else:
        return jsonify({'errors': 'There is no this category'})
    job.id = request.json['id']
    job.team_leader = request.json['team_leader']
    job.job = request.json['job']
    job.work_size = request.json['work_size']
    job.collaborators = request.json['collaborators']
    job.start_date = datetime.datetime.now()
    job.is_finished = request.json['is_finished']
    job.category_id = request.json['category_id']
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_news(jobs_id):
    db_sess = create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def put_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in ['id', 'team_leader', 'job', 'work_size', 'collaborators',
                         'is_finished', 'category_id'] for key in request.json):
        return jsonify({'error': 'Bad request'})
    print(1)
    db_sess = create_session()
    job = db_sess.query(Jobs).get(request.json['id'])

    for key in request.json:
        if key == 'category':
            category = db_sess.query(Category).filter(Category.id == request.json['category_id']).first()
            if category:
                job.category = category
            else:
                return jsonify({'errors': 'There is no this category'})

        job[key] = request.json['key']

    db_sess.merge(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
