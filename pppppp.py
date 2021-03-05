from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    params = dict()
    params['name'] = prof
    params['title'] = 'Заготовка'
    return render_template('tren.html', **params)


@app.route('/')
@app.route('/index')
def index():
    params = dict()
    params['title'] = 'Заготовка'
    return render_template('base.html', **params)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=11)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
