import json

import allure
import requests

url = 'https://api.chucknorris.io/jokes/'
expected_get_status_code = 200


class Test_ChuckNorris_Api:
    # part 1

    @allure.title("Verify Get Request Status Code")
    @allure.description("This test verify that the request passed successfully")
    def test_01_get_categories(self):
        categories_list = 'categories'
        response = requests.get(url + categories_list)
        result = response.json()
        print(json.dumps(result, indent=2))
        assert str(response.status_code) == str(404)



    @allure.title("Check Barack and Sheen Jokes")
    @allure.description("This test verify that Barack and Sheen have an equal number of jokes")
    def test_02_chuck_norris(self):
        barack_jokes_size = self.get_search_size('Barack Obama')
        sheen_jokes_size = self.get_search_size('Barack Obama')
        if (barack_jokes_size > sheen_jokes_size):
            print("Barack has more jokes than Sheen: ")
        elif (barack_jokes_size < sheen_jokes_size):
            print("Sheen has more jokes than Barack: ")
        else:
            print("Equals Number Of Jokes!")



    @allure.step("Get the total number of results")
    def get_search_size(self, seach_query):
        search_url = 'search'
        params = dict(query=seach_query)
        response = requests.get(url + search_url, params)
        return response.json()['total']
