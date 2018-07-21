from json import dumps

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

names = ['naga', 'sai', 'manoj']


@app.after_request
def after_requests(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/', methods=['GET'])
def home_page():
    return dumps(names)


app.run()
