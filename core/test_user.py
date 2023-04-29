from extends.api_core_user import ApiCoreUser
from extends.api_staff import ApiStaff


def test_post_core_user(
        email, password, infosystems, organization,
        rand_first_name,
        rand_last_name, phone_number, is_staff, work_position,
        position, department, is_active, window
):
    post_core_user = ApiCoreUser().post_core_user(
        email, password, infosystems,
        organization,
        rand_first_name,
        rand_last_name, phone_number,
        is_staff, work_position
    )
    assert post_core_user.status_code == 201
    data = post_core_user.json()
    print(post_core_user.json())
    core_id = data['id']

    # patch_core_user = ApiCoreUser().patch_core_user(core_id,
    #                                                 current_organization)
    # print(patch_core_user.json())
    # print(patch_core_user.text)
    # assert patch_core_user.status_code == 200
    # print(patch_core_user.json())
    # print(patch_core_user.text)

    post_staff = ApiStaff().post_staff(
        core_id, email, position,
        department, is_active, window
    )
    assert post_staff.status_code == 201
    print(post_staff.json())
    print(post_staff.text)
