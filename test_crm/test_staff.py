import pytest

from extends.api_staff import ApiStaff


def test_post_staff(get_core_user, position, department, is_active, window):
    post_staff = ApiStaff().post_staff(get_core_user, position,
                                       department, is_active, window)
    assert post_staff.status_code == 201
    print(post_staff.json())
    print(post_staff.text)
    return post_staff

