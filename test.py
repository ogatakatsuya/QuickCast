import requests

API_KEY = '7737025f668c0d4718e526c348467778' # 自分のAPIキーに置き換えてください。 

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
PARAMS = {
    'q': 'Tokyo,JP',  # 東京都
    'units': 'metric',  # 温度を摂氏で取得
    'appid': API_KEY
}

response = requests.get(BASE_URL, params=PARAMS)
data = response.json()

if response.status_code == 200:
    main_data = data['main']
    weather_data = data['weather'][0]
    print(f"都市: {data['name']}")
    print(f"気温: {main_data['temp']}℃")
    print(f"気圧: {main_data['pressure']} hPa")
    print(f"湿度: {main_data['humidity']}%")
    print(f"天気: {weather_data['description']}")
else:
    print(f"エラー: {data['message']}")
