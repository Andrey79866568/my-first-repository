from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет!</title>
                  </head>
                  <body>
                    <h1 align="center" style="color:#000000">Результаты отбора</h1>
                    <h3 align="center" style="color:#ffcc00">Претендента на участие в миссии {nickname}<h3>
                    <div class="alert alert-danger" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-warning" role="alert">
                        составляет {rating}!
                    </div>
                    <div class="alert alert-success" role="alert">
                        Желаем удачи!
                    </div>
                  </body>
                </html>
                    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
