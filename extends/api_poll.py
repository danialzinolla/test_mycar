from extends.api import Api
import requests


class ApiPoll(Api):
    def get_poll_list(self):
        response = requests.get(f"{self.host}/api/v1/spk/poll/",
                                headers=self.headers_type, verify=False)
        return response

    def post_poll(self, lead, client_id, status_poll, city, kind_poll,
                  issue_at, organization, service, managers, author, options,
                  autos, manager_dms):
        data = {"lead": lead, "client_id": client_id, "status": status_poll,
                "city": city, "kind": kind_poll, "issue_at": issue_at,
                "organization": organization,
                "service": service, "managers": managers, "author": author,
                "options": options, "autos": autos, "preferences": [],
                "manager_dms": manager_dms}
        response = requests.post(f"{self.host}/api/v1/spk/poll/",
                                 headers=self.headers_type, verify=False,
                                 json=data)
        return response

    def poll_to_processing(self, id):
        response = requests.post(f"{self.host}/api/v1/spk/poll/{id}/to-processing/",
                                 headers=self.headers_type, verify=False)
        return response



