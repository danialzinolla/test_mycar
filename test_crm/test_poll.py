from extends.api_poll import ApiPoll


def test_poll_list():
    poll_list = ApiPoll().get_poll_list()
    assert poll_list.status_code == 200
    print(poll_list)
    return poll_list


def test_post_poll(lead, client_id, status_poll, city, kind_poll, issue_at,
                  organization, service, managers, author, options, autos,
                  manager_dms):
    post_poll = ApiPoll().post_poll(lead, client_id, status_poll, city,
                                    kind_poll, issue_at, organization, service,
                                    managers, author, options, autos,
                                    manager_dms)
    assert post_poll.status_code == 201, post_poll.json()
    print(post_poll.text)
    return post_poll


def test_post_poll_to_processing(lead, client_id, status_poll, city, kind_poll,
                                 issue_at, organization, service, managers,
                                 author, options, autos,
                  manager_dms):
    post_poll = ApiPoll().post_poll(lead, client_id, status_poll, city,
                                    kind_poll, issue_at, organization,
                                    service, managers, author, options,
                                    autos, manager_dms)
    assert post_poll.status_code == 201
    post_poll.json()
    data = post_poll.json()
    post_poll_id = data['id']

    post_poll_to_processing = ApiPoll().poll_to_processing(post_poll_id)
    assert post_poll_to_processing.status_code == 200






