from flask import Flask, render_template, request

app = Flask(__name__)

userList = []


@app.route("/", methods=['POST', 'GET'])
def hello():

    if request.method == 'POST':
        uname = request.form['uname']
        userList.append(uname)

    return render_template('home.html', content=userList)


app.run()
