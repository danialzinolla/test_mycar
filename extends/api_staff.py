import requests
from extends.api import Api


class ApiStaff(Api):
    def post_staff(self, core_id, email, position, department, is_active,
                   window):
        data = {"user_id": core_id, "email": email, "position": position,
                "department": department, "is_active": is_active,
                "window": window}
        response = requests.post(f"{self.host}/api/v1/staff/",
                                 headers=self.headers_type, verify=False,
                                 json=data)
        return response

