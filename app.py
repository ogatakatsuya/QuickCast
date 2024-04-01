from flask import Flask,render_template,request,url_for,redirect
from forms import City
import requests
from pprint import pprint
import json
from datetime import datetime, timedelta, timezone

app = Flask(__name__, static_folder='./templates/images')

import os
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/",methods=["POST","GET"])
def search():
    form = City()
    if request.method == "POST":
        
        city = form.city.data
        API_KEY = '7737025f668c0d4718e526c348467778' # 自分のAPIキーに置き換えてください。 
        BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
        PARAMS = {
            'q': f'{city},JP',  # 東京都
            'units': 'metric',  # 温度を摂氏で取得
            'appid': API_KEY,
            'lang': 'ja'
        }
        response = requests.get(BASE_URL, params=PARAMS)
        datas = response.json()
        tz = timezone(timedelta(hours=+9),"JST")
        
        city = datas['city']['name']
        
        all_data_list = []

        for index,data in enumerate(datas['list']):
            
            if(index == 0):
                date = data['dt_txt']
                temp = round(data['main']['temp'])
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']
                icon = 'images/' + data['weather'][0]['icon'] + '.svg'
                
                first_data = {
                    'date': date,
                    'temp': temp,
                    'humidity': humidity,
                    'description': description,
                    'icon': icon
                }
                
                continue
            
            date = data['dt_txt']
            temp = round(data['main']['temp'])
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            icon = 'images/' + data['weather'][0]['icon'] + '.svg'
            
            single_data = {
                'date': date,
                'temp': temp,
                'humidity': humidity,
                'description': description,
                'icon': icon
            }
            
            all_data_list.append(single_data)
        return render_template('result.html',city = city, list = all_data_list, first_data = first_data)
    
    return render_template('search.html',form = form)

if __name__ == "__main__":
    app.run(debug=True)