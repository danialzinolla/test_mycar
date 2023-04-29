from extends.api_requests import ApiRequests
from extends.api_clients import ApiClients



def test_clients_list():
    clients_list = ApiClients().get_clients()
    assert clients_list.status_code == 200
    print(clients_list.json())
    return clients_list


def test_requests_list():
    requests_list = ApiRequests().get_requests_list()
    assert requests_list.status_code == 200
    requests_list = requests_list.json()
    print(requests_list)
    return requests_list


def test_create_requests(rand_first_name, phone_number, lead, options,
                         organization, service, managers, author, referral):
    create_clients = ApiClients().create_clients(rand_first_name, phone_number)
    assert create_clients.status_code == 200
    data = create_clients.json()
    client_id = data['id']

    post_create_requests = ApiRequests().post_requests(lead, client_id,
                                                  organization, service,
                                                  managers, author, options,
                                                  referral)
    assert post_create_requests.status_code == 201, post_create_requests.text


def test_processing_requests(rand_first_name, phone_number, lead, options,
                         organization, service, managers, author, referral):
    create_clients = ApiClients().create_clients(rand_first_name, phone_number)
    assert create_clients.status_code == 200
    data = create_clients.json()
    client_id = data['id']

    post_create_requests = ApiRequests().post_requests(lead, client_id,
                                                  organization, service,
                                                  managers, author, options,
                                                  referral)
    assert post_create_requests.status_code == 201, post_create_requests.text
    data = post_create_requests.json()
    post_create_requests = data['id']

    processing_requests = ApiRequests().post_requests_id_to_process(post_create_requests)
    assert processing_requests.status_code == 200, processing_requests.text


def test_transact_requests(rand_first_name, phone_number, lead, options,
                         organization, service, managers, author, referral,
                           expire_at):
    create_clients = ApiClients().create_clients(rand_first_name, phone_number)
    assert create_clients.status_code == 200
    data = create_clients.json()
    client_id = data['id']

    post_create_requests = ApiRequests().post_requests(lead, client_id,
                                                  organization, service,
                                                  managers, author, options,
                                                  referral)
    assert post_create_requests.status_code == 201, post_create_requests.text
    data = post_create_requests.json()
    post_create_requests = data['id']

    processing_requests = ApiRequests().post_requests_id_to_process(
        post_create_requests)
    assert processing_requests.status_code == 200, processing_requests.text

    transact_requests = ApiRequests().post_requests_id_to_transact(
        post_create_requests, expire_at)
    assert transact_requests.status_code == 200, transact_requests.text


def test_pause_requests(rand_first_name, phone_number, lead, options,
                        organization, service, managers, author, referral,
                        reason_pause, comment, expire_at):
    create_clients = ApiClients().create_clients(rand_first_name, phone_number)
    assert create_clients.status_code == 200
    data = create_clients.json()
    client_id = data['id']

    post_create_requests = ApiRequests().post_requests(lead, client_id,
                                                  organization, service,
                                                  managers, author, options,
                                                  referral)
    assert post_create_requests.status_code == 201, post_create_requests.text
    data = post_create_requests.json()
    post_create_requests = data['id']

    processing_requests = ApiRequests().post_requests_id_to_process(post_create_requests)
    assert processing_requests.status_code == 200, processing_requests.text

    pause_requests = ApiRequests().post_requests_id_to_pause(post_create_requests,
                                                             reason_pause,
                                                             comment,
                                                             expire_at)
    assert pause_requests.status_code == 200, pause_requests.text


def test_cancel_requests(rand_first_name, phone_number, lead, options,
                        organization, service, managers, author, referral,
                        reason_cancel, comment, expire_at):
    create_clients = ApiClients().create_clients(rand_first_name, phone_number)
    assert create_clients.status_code == 200
    data = create_clients.json()
    client_id = data['id']

    post_create_requests = ApiRequests().post_requests(lead, client_id,
                                                  organization, service,
                                                  managers, author, options,
                                                  referral)
    assert post_create_requests.status_code == 201, post_create_requests.text
    data = post_create_requests.json()
    post_create_requests = data['id']

    processing_requests = ApiRequests().post_requests_id_to_process(post_create_requests)
    assert processing_requests.status_code == 200, processing_requests.text

    cancel_requests = ApiRequests().post_requests_id_to_cancel(post_create_requests,
                                                               reason_cancel,
                                                               comment,
                                                               expire_at)
    assert cancel_requests.status_code == 200, cancel_requests.text


def test_delete_requests(rand_first_name, phone_number, lead, options,
                        organization, service, managers, author, referral,
                        reason_cancel, comment, expire_at):
    create_clients = ApiClients().create_clients(rand_first_name, phone_number)
    assert create_clients.status_code == 200
    data = create_clients.json()
    client_id = data['id']

    post_create_requests = ApiRequests().post_requests(lead, client_id,
                                                  organization, service,
                                                  managers, author, options,
                                                  referral)
    assert post_create_requests.status_code == 201, post_create_requests.text
    data = post_create_requests.json()
    post_create_requests = data['id']

    processing_requests = ApiRequests().post_requests_id_to_process(post_create_requests)
    assert processing_requests.status_code == 200, processing_requests.text

    cancel_requests = ApiRequests().post_requests_id_to_cancel(post_create_requests,
                                                               reason_cancel,
                                                               comment,
                                                               expire_at)
    assert cancel_requests.status_code == 200, cancel_requests.text

    delete_requests = ApiRequests().delete_requests(post_create_requests)
    assert delete_requests.status_code == 204, delete_requests.text


def test_get_requests_count():
    requests_count = ApiRequests().get_requests_count()
    assert requests_count.status_code == 200, requests_count.json()
    return requests_count








































# Вытащить список заявок
# def test_get_requests_list():
#     requests_list = ApiRequests().get_requests_list()
#     assert requests_list.status_code == 200
#     requests_list = requests_list.json()
#     print(requests_list)
#     return requests_list
#
#
# def test_get_random_requests_id():
#     requests_list = ApiRequests().get_requests_list()
#     assert requests_list.status_code == 200
#     requests_list = requests_list.json()
#     requests_id = []
#     for i in requests_list['results']:
#         id_request = i['id']
#         requests_id.append(id_request)
#     requests_id.sort()
#     requests_id = random.choice(requests_id)
#     print(requests_id)
#     return requests_id
#
#
# # def test_get_random_requests_status_code_200():
# #     requests_response = ApiRequests().get_requests_list()
# #     assert requests_response.status_code == 200
# #     requests_response = requests_response.json()
# #     requests = requests_response['results']
# #     requests_id = [i['id'] for i in requests if i['status'] == 200]
# #     print(requests_id)
# #     random_id = random.choice(requests_id)
# #     print(random_id)
# #     return random_id
#
#
# @pytest.mark.parametrize('get_random_id', [1814])
# def test_get_requests_id(get_random_id):
#     requests_id = ApiRequests().get_requests_id(get_random_id)
#     assert requests_id.status_code == 200
#     requests_id = requests_id.json()
#     print(requests_id)
#     return requests_id
# #
#
# @pytest.mark.parametrize('get_random_id', [1738, 1737])
# def test_get_requests_id_possible_transitions(get_random_id):
#     requests_id_possible_transitions = ApiRequests().\
#         get_requests_id_possible_transitions(get_random_id)
#     assert requests_id_possible_transitions.status_code == 200
#     requests_id_possible_transitions = requests_id_possible_transitions.json()
#     print(requests_id_possible_transitions)
#     return requests_id_possible_transitions
#
#
# def test_get_requests_count():
#     requests_count = ApiRequests().get_requests_count()
#     assert requests_count.status_code == 200
#     requests_count = requests_count.json()
#     print(requests_count)
#     return requests_count
#
#
# #def test_get_requests_report(start_date, end_date):
# #    requests_report = ApiRequests().get_requests_report(start_date, end_date)
# #   assert requests_report.status_code == 200
# #    requests_report = requests_report.json()
# #    print(requests_report)
# #    return requests_report
#
# def test_get_requests_report_appeals():
#     requests_report_appeals = ApiRequests().get_requests_report_appeals()
#     assert requests_report_appeals.status_code == 200
#     #requests_report_appeals = requests_report_appeals.json()
#     print(requests_report_appeals)
#     return requests_report_appeals
#
#
# @pytest.mark.parametrize('get_random_id', [1739])
# def test_get_requests_report_appeals_id(get_random_id):
#     requests_report_appeals_id = ApiRequests().get_requests_report_appeals_id(
#         get_random_id)
#     assert requests_report_appeals_id.status_code == 200
#     #requests_report_appeals_id = requests_report_appeals_id.json()
#     print(requests_report_appeals_id)
#     return requests_report_appeals_id
#
#
# def test_get_requests_report_poll_sale():
#     requests_report_poll_sale = ApiRequests().get_requests_report_poll_sale()
#     assert requests_report_poll_sale.status_code == 200
#     print(requests_report_poll_sale)
#     return requests_report_poll_sale
#
#
# def test_get_requests_report_poll_service():
#     requests_report_poll_service = \
#         ApiRequests().get_requests_report_poll_service()
#     assert requests_report_poll_service.status_code == 200
#     print(requests_report_poll_service)
#     return requests_report_poll_service
#
#
# def test_post_requests(lead, test_post_natural_client, options,
#                        organization, service, author):
#     requests_post = ApiRequests().post_requests(
#                                                 lead, test_post_natural_client,
#         options, organization, service, author)
#     print(curlify.to_curl(requests_post.request, compressed=False))
#     assert requests_post.status_code == 201, requests_post.text
#     print(requests_post.text)
#     return requests_post
#
#
# def test_post_requests_id_to_create():
#     post_requests_id_to_create = ApiRequests().post_requests_id_to_create()
#     assert post_requests_id_to_create.status_code == 200, \
#         post_requests_id_to_create.text
#     post_requests_id_to_create = post_requests_id_to_create.json()
#     print(post_requests_id_to_create)
#     return post_requests_id_to_create
#
#
# def test_post_requests_id_to_process():
#     post_requests_id_to_process = ApiRequests().post_requests_id_to_process()
#     assert post_requests_id_to_process.status_code == 200, post_requests_id_to_process.text
#     post_requests_id_to_process = post_requests_id_to_process.json()
#     print(post_requests_id_to_process)
#     return post_requests_id_to_process
#
#
# # @pytest.mark.parametrize('get_random_id', [1814])
# # def test_post_to_create_and_process(get_random_id, expire_at):
# #     post_to_create = ApiRequests().post_requests_id_to_create(get_random_id, expire_at)
# #     assert post_to_create.ok
# #     post_to_process = ApiRequests().post_requests_id_to_process(get_random_id, expire_at)
# #     post_to_process.status_code == 200
#
#
# @pytest.mark.parametrize('get_random_id', [1814])
# def test_post_requests_id_to_pause(get_random_id, reason, comment, expire_at):
#     post_requests_id_to_pause = ApiRequests().post_requests_id_to_pause(
#         get_random_id, reason, comment, expire_at)
#     assert post_requests_id_to_pause.status_code == 200, \
#         post_requests_id_to_pause.text
#     post_requests_id_to_pause = post_requests_id_to_pause.json()
#     print(post_requests_id_to_pause)
#     return post_requests_id_to_pause
#
#
# @pytest.mark.parametrize('get_random_id', [1814])
# def test_post_requests_id_to_cancel(get_random_id, reason, comment, expire_at):
#     post_requests_id_to_cancel = ApiRequests().post_requests_id_to_cancel(
#         get_random_id, reason, comment, expire_at)
#     assert post_requests_id_to_cancel.status_code == 200, \
#         post_requests_id_to_cancel.text
#     post_requests_id_to_cancel = post_requests_id_to_cancel.json()
#     print(post_requests_id_to_cancel)
#     return post_requests_id_to_cancel
#
#
# @pytest.mark.parametrize('get_random_id', [1814])
# def test_post_requests_id_to_transact(get_random_id, expire_at):
#     post_requests_id_to_transact = ApiRequests().post_requests_id_to_transact(
#         get_random_id, expire_at)
#     assert post_requests_id_to_transact.status_code == 200, \
#         post_requests_id_to_transact.text
#     post_requests_id_to_transact = post_requests_id_to_transact.json()
#     print(post_requests_id_to_transact)
#     return post_requests_id_to_transact


