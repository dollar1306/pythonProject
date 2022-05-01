import json
import requests
from requests.auth import HTTPBasicAuth
auth=HTTPBasicAuth('admin', 'admin')

class Test_Grafana:
    def test_print_teams(self):
        url = 'http://localhost:3000/'
        resources = 'api/teams/search'
        response = requests.get(url + resources, auth=auth)
        res_json = response.json()
        # print(json.dumps(res_json, indent=2))
        for name_of_team in response.json()["teams"]:
            print("\nName: " +str(name_of_team["name"]))
        assert response.status_code == 200