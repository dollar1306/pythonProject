import json

import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = 'ad48510a9aed1ff96b51557d94bc5964'
city = 'london,uk'



def test_weather():
    params = dict(appid = api_key, q = city, units = 'metric')
    response = requests.get(url, params)
    #print(response)
    response_json = response.json()
    print(json.dumps(response_json, indent=2))

    #print(response.text())