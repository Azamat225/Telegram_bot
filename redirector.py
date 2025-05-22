from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

# Маршрут для отдачи APK
@app.route('/download/apk')
def download_apk():
    return send_from_directory(directory='static/apk', path='app-release.apk')

@app.route('/vpn/<uuid:_id>/<name>')
def vpn_redirect(_id, name):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Redirecting...</title>
    <a href="aza://{{_id}}&name={{name}}">сюда</a>
</head>
<body>
    <h2>Подключение к VPN</h2>
    <p>Если приложение не открылось автоматически — нажмите на одну из кнопок ниже:</p>

    <button onclick="window.location.href='aza://{_id}&name={name}'">Открыть приложение</button>
    <br><br>
    <p id="fallback" style="display:none;">
    <a href="/download/apk"><button>⬇️ Скачать APK</button></a><br>
    Или нажмите <a href="aza://{{_id}}&name={{name}}">сюда</a>, чтобы открыть приложение.
</p>

    <p style="margin-top: 20px; font-size: 0.9em;">
        Убедитесь, что у вас разрешена установка приложений из неизвестных источников.
    </p>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)