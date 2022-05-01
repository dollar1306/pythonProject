import json

import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = 'ad48510a9aed1ff96b51557d94bc5964'
city = 'jerusalem,il'


class Test_API_Requests:

    def setup_class(self):
        params = dict(appid=api_key, q=city, units='metric')
        global response
        response = requests.get(url, params)

    def test_get_request(self):
        # part1
        # params = dict(appid=api_key, q=city, units='metric')
        # response = requests.get(url, params)
        result = response.json()

        print("\nThe code of response is:", response)
        print(json.dumps(result, indent=2))

        # print(response.request) #GET

        print(response.headers['Date'])
        print(response.status_code)
        print(response.headers)

        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_assert_status_code(self):
        assert response.status_code == 200

    def test_request_city(self):

        # part 2
        result = response.json()
        print("The name of city is: ", result['name'])
        assert result['sys']['country'] == 'IL'
        print("The country is:", result['sys']['country'])

        #part3
        humidity_api = result['main']['humidity']
        print("Humidity is:", humidity_api)


