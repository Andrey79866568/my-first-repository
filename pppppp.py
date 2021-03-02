from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1 align="center" style="color:#000000">Загрузка фотографии</h1>
                            <h3 align="center" style="color:#000000">для участия в миссии </h3>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Приложите фотографию.</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        <label>~~~~~~~~~~~~~~~~~~~~~~~~</label>
                                        <img src="{url_for('static', filename='images/robot.jpg')}" 
                                            alt="здесь должна была быть картинка, но не нашлась">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open(os.path.join('static', 'images',  'request_image.jpg'), 'wb') as file:
            for i in f.readlines():
                file.write(i)
        return f'''<img src="{url_for('static', filename='images/request_image.jpg')}">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
