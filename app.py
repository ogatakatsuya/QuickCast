from flask import Flask,render_template,request,url_for,redirect
from forms import City
import requests

app = Flask(__name__)

import os
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/",methods=["POST","GET"])
def search():
    form = City()
    if request.method == "POST":
        city = form.city.data
        API_KEY = '7737025f668c0d4718e526c348467778' # 自分のAPIキーに置き換えてください。 

        BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
        PARAMS = {
            'q': f'{city},JP',  # 東京都
            'units': 'metric',  # 温度を摂氏で取得
            'appid': API_KEY
        }
        response = requests.get(BASE_URL, params=PARAMS)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            weather = data["weather"][0]["main"]
            return render_template('result.html',temp=temp,humidity=humidity,wind=wind,weather=weather)
        else:
            print(f"エラー: {data['message']}")
    return render_template('search.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)