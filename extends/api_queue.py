import requests
from extends.api import Api


class ApiQueue(Api):
    def get_queue_list(self):
        response = requests.get(f"{self.host}/api/v1/queue/", headers=self.headers_type, verify=False)
        print(response)
        return response

    def post_queue_list(self, get_random_request_id, notification_service, print_ticket):
        data = {'request': get_random_request_id, 'notification_service': notification_service,
                'print_ticket': print_ticket}
        response = requests.post(f"{self.host}/api/v1/queue/", headers=self.headers_type, json=data, verify=False)
        print(response)
        return response
