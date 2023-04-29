import requests as requests
from extends.api import Api


class ApiClients(Api):
    def get_clients(self):
        response = requests.get(f"{self.host_clients}/clients/",
                                headers=self.headers_type, verify=False)
        return response
        # url = f"{self.host_clients}/clients/?search=73294876589&limit=10"
        #
        # response = requests.get(url=url)
        # return response

    def create_clients(self, rand_first_name, phone_number):
        # url = f"{self.host_clients}/v2/clients/natural_client/"
        data = {
            "natural_client": {"first_name": rand_first_name},
            "client_phones": [{"phone": phone_number}]
        }
        response = requests.post(f"{self.host_clients}/v2/clients/natural_client/",
                                headers=self.headers_type, verify=False,
                                json=data)
        # response = requests.post(url=url, json=data)
        return response
