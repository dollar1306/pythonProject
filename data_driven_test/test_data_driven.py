import allure
import pytest

import requests

keys = "url, expected_status_code"

values = [("http://google.com", "200"), ("http://imdb.com", "200"), ("http://imdb.com/123", "404"), ("http://supplant.me/bot", "400")]


class Test_DDT_URL:
    @allure.title("Verify Get Request Status Code")
    @allure.description("This test verify that the request passed successfully")
    @pytest.mark.parametrize(keys, values)
    def test_status_code(self, url, expected_status_code):
        response = requests.get(url)
        assert response.status_code == int(expected_status_code)