import pytest
import requests
from extends.api import Api


class ApiCoreUser(Api):
    def post_core_user(self, email, password, infosystems, organization,
                       rand_first_name,
                       rand_last_name, phone_number, is_staff, work_position):
        data = {"email": email, "password": password,
                "infosystems": infosystems,
                "organizations": organization, "first_name": rand_first_name,
                "last_name": rand_last_name, "phone": phone_number,
                "is_staff": is_staff,
                "work_position": work_position}
        response = requests.post(f"{self.host_core}/auth/users/",
                                 headers=self.headers_type, verify=False,
                                 json=data)
        return response

    def get_core_user(self, id):
        response = requests.get(f"{self.host_core}/auth/users/{id}/",
                                headers=self.headers_type, verify=False)

        print(response)
        return response

    def patch_core_user(self, id, current_organization):
        data = {"current_organization": current_organization}
        response = requests.patch(f"{self.host_core}/auth/users/{id}/",
                                headers=self.headers_type, verify=False,
                                  json=data)
        print(response)
        return response