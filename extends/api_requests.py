import requests
from extends.api import Api


class ApiRequests(Api):
    def get_requests_list(self):
        response = requests.get(f"{self.host}/api/v1/requests/",
                                headers=self.headers_type, verify=False)
        return response

    def get_requests_id(self, id):
        response = requests.get(f"{self.host}/api/v1/requests/{id}/",
                                headers=self.headers_type, verify=False)
        return response

    # # def get_requests_id_possible_transitions(self, id):
    # #     response = requests.get(f"{self.host}/api/v1/requests/{id}/possible-transitions/",
    # #                             headers=self.headers_type,
    # #                             verify=False)
    #     return response

    def get_requests_count(self):
        response = requests.get(f"{self.host}/api/v1/requests/count/",
                                headers=self.headers_type,
                                verify=False)
        return response

    def post_requests(self, lead, client_id, organization, service, managers,
                      author, options, referral):
        data = {"lead": lead, "client_id": client_id,
                "organization": organization, "service": service,
                "managers": managers, "author": author, "options": options,
                "referral": referral}
        response = requests.post(f'{self.host}/api/v1/requests/',
                                 headers=self.headers_type, verify=False,
                                 json=data)
        return response

    def post_requests_id_to_create(self, id, expire_at):
        data = {"expire_at": expire_at}
        response = requests.post(f"{self.host}/api/v1/requests/{id}/to-create/",
                                 headers=self.headers_type, verify=False,
                                 json=data)
        return response

    def post_requests_id_to_process(self, id):
        response = requests.post(f"{self.host}/api/v1/requests/{id}/to-process/"
                                 , headers=self.headers_type,
                                 verify=False)
        return response

    def post_requests_id_to_pause(self, id, reason_pause, comment, expire_at):
        data = {"reason": reason_pause, "comment": comment,
                "expire_at": expire_at}
        response = requests.post(f"{self.host}/api/v1/requests/{id}/to-pause/",
                                 headers=self.headers_type,
                                 verify=False, json=data)
        return response

    def post_requests_id_to_cancel(self, id, reason_cancel, comment, expire_at):
        data = {"reason": reason_cancel, "comment": comment,
                "expire_at": expire_at}
        response = requests.post(f"{self.host}/api/v1/requests/{id}/to-cancel/",
                                 headers=self.headers_type,
                                 verify=False, json=data)
        return response

    def post_requests_id_to_transact(self, id, expire_at):
        data = {"expire_at": expire_at}
        response = requests.post(f"{self.host}/api/v1/requests/{id}/to-transact/",
                                 headers=self.headers_type,
                                 verify=False, json=data)
        return response

    def delete_requests(self, id):
        response = requests.delete(f"{self.host}/api/v1/requests/{id}/",
                                   headers=self.headers_type, verify=False)
        return response
