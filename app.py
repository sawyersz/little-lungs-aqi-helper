from flask import Flask
import json
import requests

app = Flask(__name__)
api_key = 'eaa3b405-c5ba-42ea-8344-65b361b06449'

@app.route("/")
def location():
    lat=52.1470
    lon=21.0840
    payload = {'lat':lat, 'lon':lon, 'key':api_key}
    resp = requests.get('http://api.airvisual.com/v2/nearest_city', params=payload)
    return resp.json()

if __name__ == '__main__':
    app.run(debug=True)