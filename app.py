from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods =['POST', 'GET'])
def get_weatherdata():
    api_key = "f506e4efbe2cb47a1738679fc38876f6"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q":request.form.get('city', 'country_code'), "appid" : api_key}
    response = requests.get(url, params=params)
    data = response.json()
    return (data)



if __name__ == '__main__':
    app.run()