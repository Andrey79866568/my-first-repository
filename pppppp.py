from flask import Flask, url_for, request

app = Flask(__name__)
list_ik = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']


@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс</h1>
           <img src="{url_for('static', filename='images/Mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
           дак вот ты какая, красная планета'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center" style="color:#000000">Анкета претендента</h1>
                            <h4 align="center" style="color:#000000">на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label> </label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="from-group">
                                        <label for="classSelect">Какое у вас образоване?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Несколько высших</option>
                                          <option>Я сверхразум и без образования</option>
                                        </select>
                                    </div>
                                    <label> </label>
                                    <div class="from-group">
                                        <label for="profs">Кем вы можете себя назвать?</label>
                                        
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profs" id="инженер-исследователь" value="инженер-исследователь">
                                          <label class="form-check-label" for="инженер-исследователь">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profs" id="пилот" value="пилот">
                                          <label class="form-check-label" for="пилот">
                                            пилот
                                          </label>
                                        </div>
                                        
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profs" id="строитель" value="строитель">
                                          <label class="form-check-label" for="строитель">
                                            строитель
                                          </label>
                                        </div>
                                    </div>
                                    <label> </label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <label> </label>
                                    <div class="form-group">
                                        <label for="about">Почему вы решили учавствовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="4" name="about"></textarea>
                                    </div>
                                    <label> </label>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <label> </label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept_to_stay">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form)
        return "Форма отправлена"


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '</br>'.join(list_ik)


@app.route('/promotion_image')
def image_prom():
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
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='images/Mars.jpg')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-danger" role="alert">
                        {list_ik[0]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                        {list_ik[1]}
                    </div>
                    <div class="alert alert-success" role="alert">
                        {list_ik[2]}
                    </div>
                    <div class="alert alert-info" role="alert">
                        {list_ik[3]}
                    </div>
                    <div class="alert alert-primary" role="alert">
                        {list_ik[4]}
                    </div>
                  </body>
                </html>
                    '''


@app.route('/tren')
def tren():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route('/bootstrap_sample')
def bootstrap():
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
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-warning" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
