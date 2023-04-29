from locust import HttpUser, between, task
from extends.api import Api
import os
from extends.api_requests import ApiRequests
from requests.auth import HTTPBasicAuth
import requests
import curlify


class QuickstartUser(HttpUser):
    token = None
    wait_time = between(1, 3)

    def on_start(self):
        data = {"email": "l.pan@mycar.kz", "password": "mycar1234"}
        headers_type = {'Content-Type': 'application/json'}
        response = requests.post("https://api.core.sandbox.mycarpro.net/auth/jwt/create/", headers=headers_type,
                                 json=data,
                                 verify=False)
        result = response.json()
        self.token = result['access']
        print(self.token)

    @task(1)
    def download_report_polls_list(self):
        headers_type = {'Authorization': "Bearer" + " " + self.token}
        response = self.client.get("https://api.crm.sandbox.mycarpro.net/api/v1/reports/polls/list_excel/",
                                   headers=headers_type, verify=False)
        print(curlify.to_curl(response.request, compressed=True))
        print(response.text)
        print(response.status_code)


