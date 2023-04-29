import requests as requests


class Api:
    host = None
    data_user = None

    def __init__(self):
        self.host = "https://api.crm.sandbox.mycarpro.net"
        self.host_core = "https://api.core.sandbox.mycarpro.net"
        self.data_user = self.authorize
        self.token = f"Bearer {self.data_user()}"
        self.headers_type = {"Content-Type": "application/json",
                             "Authorization": self.token}
        self.host_clients = "https://api.clients.sandbox.mycarpro.net"

    def login(self):
        data = {"email": "l.pan@mycar.kz", "password": "mycar1234"}
        headers_type = {"Content-Type": "application/json"}
        response = requests.post("https://api.core.sandbox.mycarpro.net/auth/jwt/create/", headers=headers_type,
                                 json=data, verify=False)
        return response

    def authorize(self):
        response = self.login()
        if response.status_code != 200:
            raise Exception("Error authorize using given credential")
        result = response.json()
        print(result)
        result = result["access"]
        return result




