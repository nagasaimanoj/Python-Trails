from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return "<h1>Hello Flask</h1>"


app.run(host='0.0.0.0', port=80)
