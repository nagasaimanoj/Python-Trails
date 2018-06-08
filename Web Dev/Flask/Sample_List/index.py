from flask import (Flask, redirect, render_template, request)

app = Flask(__name__)

userList = []


@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html', userList=userList)


@app.route('/addItem', methods=['POST'])
def addItem():
    uname = request.form['uname']
    userList.append(uname)
    return redirect('/')


@app.route('/deleteItem', methods=['GET'])
def deleteItem():
    name = request.args.get('name')
    userList.remove(name)
    return redirect('/')


@app.route('/editItem', methods=['GET'])
def editItem():
    name = request.args.get('name')
    userList.remove(name)
    return render_template('home.html', userList=userList, value=name)


app.run(debug=True)
