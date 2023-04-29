import pytest
import requests


@pytest.mark.parametrize('email', ['d.zinolla@mycar.kz'])
@pytest.mark.parametrize('password', ['mycar1234'])
def test_auth(email, password):
    data = {'email': email, 'password': password}
    headers_type = {"Content_type": "application/json"}
    response = requests.post('https://api.core.sandbox.mycarpro.net/auth/jwt/create', headers=headers_type, json=data,
                             verify=False)
    assert response.status_code == 200, response.text
    return response


