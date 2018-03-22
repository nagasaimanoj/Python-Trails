from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return "<h1>Hello Flask</h1>"


app.run(debug=True)
