from flask import Flask,render_template,request,url_for,redirect
from forms import City
import requests
from pprint import pprint
import json
import datetime

app = Flask(__name__, static_folder='./templates/images')

import os
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/",methods=["POST","GET"])
def search():
    form = City()
    if request.method == "POST":
        
        city = form.city.data
        API_KEY = '7737025f668c0d4718e526c348467778'
        BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
        PARAMS = {
            'q': f'{city},JP',
            'units': 'metric',
            'appid': API_KEY,
            'lang': 'ja'
        }
        response = requests.get(BASE_URL, params=PARAMS)
        datas = response.json()
        
        city = datas['city']['name']
        all_data_list = []

        for index,data in enumerate(datas['list']):
            
            if(index == 0):
                utc_timestamp = data['dt']
                jst_timestamp = utc_timestamp + 9*3600

                jst_dt = datetime.datetime.utcfromtimestamp(jst_timestamp)
                month = str(jst_dt.month).zfill(2)
                day = str(jst_dt.day).zfill(2)
                hour = str(jst_dt.hour).zfill(2)
                minute = str(jst_dt.minute).zfill(2)
                date = f"{month}/{day} {hour}:{minute}"
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
            
            utc_timestamp = data['dt']
            jst_timestamp = utc_timestamp + 9*3600

            jst_dt = datetime.datetime.utcfromtimestamp(jst_timestamp)
            month = str(jst_dt.month).zfill(2)
            day = str(jst_dt.day).zfill(2)
            hour = str(jst_dt.hour).zfill(2)
            minute = str(jst_dt.minute).zfill(2)
            date = f"{month}/{day} {hour}:{minute}"
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