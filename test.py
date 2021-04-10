from requests import get, post, delete, put

print(get('http://localhost:8080/api/jobs').json())


print(put('http://localhost:8080/api/jobs').json())

print(put('http://localhost:8080/api/jobs/993').json())

print(put('http://localhost:8080/api/jobs/sdfssaaw').json())

print(put('http://localhost:8080/api/jobs/6', json={'collaborators': 'all peoples'}).json())

'''
print(delete('http://localhost:8080/api/jobs').json())

print(delete('http://localhost:8080/api/jobs/993').json())

print(delete('http://localhost:8080/api/jobs/sdfssaaw').json())

print(delete('http://localhost:8080/api/jobs/6').json())
'''

# print(post('http://localhost:8080/api/jobs').json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'team_leader': 4}).json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'id': 2,
#                  'team_leader': 2,
#                  'job': 'adfsd',
#                  'work_size': 4,
#                  'collaborators': '2, 3, 5',
#                  'is_finished': False,
#                  'category_id': 4}).json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'id': 6,
#                  'team_leader': 4,
#                  'job': 'Тренировка в сдаче ЕГЭ!',
#                  'work_size': 5,
#                  'collaborators': 'all',
#                  'is_finished': False,
#                  'category_id': 3}).json())


print(get('http://localhost:8080/api/jobs').json())
