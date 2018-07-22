from json import dumps

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

names = []

names.append({'name': 'g', 'age': 24})
names.append({'name': 'naga', 'age': 25})
names.append({'name': 'sai', 'age': 26})
names.append({'name': 'manoj', 'age': 27})
names.append({'name': 'kumar', 'age': 28})


@app.after_request
def after_requests(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/')
def home_page():
    return render_template('/home', names=dumps(names))


@app.route('/data')
def data():
    return dumps(names)


@app.route('/add', methods=['GET'])
def add():
    uname = request.form['uname']
    uage = request.form['uage']
    names.append({'name': uname, 'age': uage})
    return redirect('/')


@app.route('/delete', methods=['GET'])
def delete():
    del_name = request.args.get('name')
    index = 0
    for each_record in names:
        if each_record['name'] == del_name:
            del names[index]
        index += 1
    return redirect('/')


app.run()
