from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            error.p {{
                color: red;
            }}
        </style>
     </head>
    <body>
        <form action="/rot" method="POST">
            <div>
                <label for="rot">Rotate By:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(encrypt)

@app.route("/rot", methods=["POST"])
def encrypt():
    rot_value = int(request.form['rot'])
    text_value = request.form['text']
    rotate = rotate_string(text_value,rot_value)
    return form.format(rotate)

app.run()