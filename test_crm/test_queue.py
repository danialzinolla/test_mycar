import pytest
from extends.api_queue import ApiQueue


def test_get_queue_list():
    queue_list = ApiQueue().get_queue_list()
    assert queue_list.status_code == 200
    queue_list = queue_list.json()
    print(queue_list)
    return queue_list


def test_post_queue(get_random_request_id, notification_service, print_ticket):
    post_queue_list = ApiQueue().post_queue_list(get_random_request_id, notification_service, print_ticket)
    assert post_queue_list.status_code == 201
    post_queue_list = post_queue_list.json()
    print(post_queue_list)
    return post_queue_list
