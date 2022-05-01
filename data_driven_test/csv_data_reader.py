import csv

import allure
import pytest
import requests


@allure.step("Get external data from CSV file and save")
def get_data_from_csv():
    list = []
    with open("data.csv", newline='') as f:
        reader = csv.reader(f)
        list = [tuple(row) for row in reader]
        return list


keys = "url, expected_status_code"


class Test_Get_Data_Url:
    @pytest.mark.parametrize(keys, get_data_from_csv())
    def test_status_code(self, url, expected_status_code):
        response = requests.get(url)
        assert response.status_code == int(expected_status_code)
