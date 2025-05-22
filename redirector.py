from flask import Flask, redirect

app = Flask(__name__)


@app.route('/vpn/<uuid:_id>/<name>')
def vpn_redirect(_id, name):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Redirecting...</title>
    <script type="text/javascript">
        window.location.href = "aza://{_id}&name={name}";
        setTimeout(() => {{
            window.location.href = "https://play.google.com/store/apps/details?id=com.example.yourapp ";
        }}, 2000);
    </script>
</head>
<body>
    Если вы не перешли автоматически — <a href="aza://{_id}&name={name}">нажмите сюда</a><br>
    Убедитесь, что у вас установлено приложение.
</body>
</html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
