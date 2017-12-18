import urllib2
# If you are using Python 3+, import urllib2 instead of urllib2

import json


data = {

    "Inputs": {

        "input1":
        {
            "ColumnNames": ["S.No", "Input", "Target"],
            "Values": [["0", "value", "value"], ["0", "value", "value"], ]
        }, },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/bc822eac64c54e1bb6b6df715f8ab943/services/02e258d9f71e4d0c9e0e66c9258cfd3f/execute?api-version=2.0&details=true'
# Replace this with the API key for the web service
api_key = '/haC7b7I37ldZrhdCfY0EjOzjiVmw0pK7Ffwnn4me7W7mXVzyGceM9wCv9QjsjDIW9wBrmMDv0jT9R8Vj9bt3g=='
headers = {'Content-Type': 'application/json',
           'Authorization': ('Bearer ' + api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib2.request in the above code:
    # req = urllib2.request.Request(url, body, headers)
    # response = urllib2.request.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError.error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
