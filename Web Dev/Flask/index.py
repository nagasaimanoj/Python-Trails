from human import human
from flask import Flask,render_template, request, jsonify

app = Flask(__name__)

userList = []
id = 1

@app.route("/")
def hello():
    return render_template('home.html', content = userList)

@app.route("/", methods=['POST'])
def hello2():
    hhh = human()
    id += 1

    hhh.setName(request.form['uname'])

    userList.append(id, hhh)

    return render_template('home.html', content = userList)

@app.route("/del", methods=['POST'])
def delete():
    del userList[request.form['uname']]

app.run(debug = True)