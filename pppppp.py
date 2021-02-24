from flask import Flask, url_for
import os

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    list_ik = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
               'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(list_ik)


@app.route('/image_sample')
def image():
    return f'''<h1>Жди нас, Марс</h1>
           <img src="{url_for('static', filename='images/Mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
           дак вот ты какая, красная планета'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
