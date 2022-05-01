import requests

url = 'http://localhost:3000'
resource = '/posts'
id = '/101'


class Test_API_Requests:
    # POST request
    def test_post_request(self):
        payload = {"userId": 11, "id": "101", "title": "test", "body": "123"}
        response = requests.post(url + resource, data=payload)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 201

    # PUT request
    def test_put_request(self):
        payload = {"userId": 11, "id": 101, "title": "Yoni", "body": "456"}
        response = requests.put(url + resource + id, data=payload)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 200

    # PATCH request
    def test_patch_request(self):
        payload = {"title": "Kuku"}
        response = requests.patch(url + resource + id, data=payload)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 200

    # DELETE request
    def test_delete_request(self):
        response = requests.delete(url + resource + id)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 200
