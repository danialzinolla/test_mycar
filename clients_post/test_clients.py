from pytest import fixture

from extends.api_clients import ApiClients


@fixture
def test_post_natural_client(
        referral_id, rand_first_name, rand_last_name, sex, phone_number,
        comment
):
    client = ApiClients()
    response = client.get_client()

    assert response.status_code == 200

    if response.json()['count'] > 0:
        client_id = response.json()['results'][0]['id']
        return client_id
