from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

# Маршрут для отдачи APK
@app.route('/download/apk')
def download_apk():
    return send_from_directory(directory='static/apk', path='app-release.apk')

@app.route('/vpn/<uuid:_id>/<name>')
def vpn_redirect(_id, name):
    deep_link = f"aza://152.114.192.9/{_id}?name={name}"
    return f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Подключение к VPN</title>
    <meta http-equiv="refresh" content="1; url={deep_link}">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f8;
            color: #333;
            text-align: center;
            padding: 50px;
        }}
        .container {{
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}
        h2 {{
            margin-bottom: 20px;
        }}
        button {{
            background-color: #007bff;
            color: white;
            border: none;
            padding: 12px 20px;
            margin-top: 10px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #0056b3;
        }}
        .fallback {{
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }}
        .download-btn {{
            background-color: #28a745;
        }}
        .download-btn:hover {{
            background-color: #1e7e34;
        }}
        a {{
            color: #007bff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Подключение к VPN</h2>
        <p>Ожидаем открытие приложения...</p>

        <button onclick="window.location.href='{deep_link}'">🔓 Открыть приложение вручную</button>

        <div class="fallback">
            <p>Если приложение не открылось:</p>
            <a href="/download/apk"><button class="download-btn">⬇️ Скачать APK</button></a><br><br>
            <p>Или нажмите <a href="{deep_link}">сюда</a>, чтобы открыть приложение вручную.</p>
        </div>

        <p style="margin-top: 30px; font-size: 13px;">
            Убедитесь, что у вас разрешена установка приложений из неизвестных источников.
        </p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)