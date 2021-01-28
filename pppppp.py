#!C:\Users\ovsia\PycharmProjects\andreysrepo\venv\Scripts\python.exe

import schedule
import datetime as dt


def job():
    flag = True
    if dt.datetime.now().second + dt.datetime.now().minute == 0 and flag:
        print('Ку')
        flag = False
    elif not dt.datetime.now().minute + dt.datetime.now().second == 0:
        flag = True


schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
