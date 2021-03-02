from flask import Flask, url_for, request

app = Flask(__name__)

dict_planet = {'Марс': ['Близка к Земле', 'На ней много ресурсов', 'На ней есть твердая земля',
                        'Какая-то атмосфера, хоть и из CO2',
                        'В целом можно и слетать'],
               'Земля': ['наша', 'Не делай вид, что не знаешь', 'идеальная планета для жизни', 'но мы и так здесь',
                         'будь я пришелец - слетал бы'],
               'Венера': ['ну такое', 'Расплавишься нафиг', 'Не думай даже', 'НЕ ПОЛЕТИМ', 'всё.']}


@app.route('/choice/<planet>')
def image_prom(planet):
    if planet in dict_planet:
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
                        <h1 align="center" style="color:#000000">Мое предложение: {planet}</h1>
                        <h3 align="center" style="color:#ffcc00">{dict_planet[planet][0]}<h3>
                        <div class="alert alert-danger" role="alert">
                            {dict_planet[planet][1]}
                        </div>
                        <div class="alert alert-warning" role="alert">
                            {dict_planet[planet][2]}
                        </div>
                        <div class="alert alert-success" role="alert">
                            {dict_planet[planet][3]}
                        </div>
                        <div class="alert alert-info" role="alert">
                            {dict_planet[planet][4]}
                        </div>
                      </body>
                    </html>
                        '''
    else:
        return 'я туда не полечу'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
