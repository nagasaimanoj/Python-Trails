import urllib.request
import json

url = urllib.request.urlopen(
    "http://maps.googleapis.com/maps/api/geocode/json?address=google")
data = json.loads(url.read().decode())

data = dict(data)