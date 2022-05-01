import json

import requests

url = 'http://localhost:9000/student'

header = {'Content-type': 'application/json'}
id = '/107'
class Test_API_Requests_Students:

    def test_get_all_students(self):
        response = requests.get(url+"/list")
        response_json = response.json()
        print(json.dumps(response_json, indent=2))

    def test_post_student(self):
        payload = {'firstName': 'Alex', 'lastName': 'Kuzmin', 'email': 'alex12@gmail.com', 'programme': 'Engineering'}
        response = requests.post(url, json=payload, headers=header)
        response_json = response.json()
        print('Response Code: ', response)
        print('Response Code: ', response_json)
        assert response.status_code == 201

    def test_put_student(self):
        payload = {'firstName': 'Alex', 'lastName': 'Kuzmin', 'email': 'alex12@gmail.com', 'programme': 'Engineering',
                   'courses': ['Java', 'C#', 'Software Development', 'Python']
                   }
        response = requests.put(url+id, json=payload, headers=header)
        response_json = response.json()
        print('Response Code: ', response)
        print('Response Code: ', response_json)
        assert response.status_code == 200

    def test_del_student(self):
        response = requests.delete(url + id)
        print(response)
        assert response.status_code == 204
