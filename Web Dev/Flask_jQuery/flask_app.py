from flask import Flask, jsonify
from json import dumps
import pandas as pd
from flask_cors import CORS

projects_csv = pd.read_csv(
    '/Users/nagasai/Manoj/Code/Python-Trails/Web Dev/Flask_jQuery/projects.csv'
)

projects_list = list(projects_csv.T.to_dict().values())


app = Flask(__name__)
CORS(app)


@app.route('/project_details')
def home_page():
    return dumps(projects_list)


app.run(host='0.0.0.0', port=80)
