import json
import xml.etree.ElementTree as ET

import requests


def get_data(node_name):
    root = ET.parse('weather.xml').getroot()
    return root.find(".//" + node_name).text

class Test_API_Requests:all

def test_API_request(self):
    params = dict()
    response = requests.get()

    response_json = response.json()
    print(json.dumps(response_json, indent=2))








