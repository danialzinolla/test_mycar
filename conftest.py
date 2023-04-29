import random
import pytest
from faker import Faker
import names
import random
import string
from faker_vehicle import VehicleProvider
from extends.api_requests import ApiRequests
from datetime import datetime
import datetime
import requests as requests
from extends.api_clients import ApiClients
from extends.api_core_user import ApiCoreUser


# lead
@pytest.fixture()
def lead(rand_first_name, phone_number):
    lead = {"name": rand_first_name, "phone": phone_number}
    print(lead)
    return lead


@pytest.fixture()
def rand_first_name():
    for i in range(10):
        rand_name = names.get_first_name(gender='male')
    return rand_name


@pytest.fixture()
def rand_last_name():
    for i in range(10):
        rand_name = names.get_last_name()
        return rand_name


@pytest.fixture()
def phone_number():
    codes = ["701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711"]
    choosing_code = random.choice(codes)
    other_numbers = random.randint(1000000, 9999999)
    phone_number = f"+7{str(choosing_code) + str(other_numbers)}"
    return phone_number


#options
@pytest.fixture()
def options(priority, kind, lang):
    options = {"priority": priority, "kind": kind, "lang": lang}
    return options


@pytest.fixture()
def priority():
    priority = ["low", "medium", "high"]
    return random.choice(priority)


@pytest.fixture()
def kind():
    kind = "offline"
    return kind


@pytest.fixture()
def lang():
    lang = "ru"
    return lang


@pytest.fixture()
def organization():
    organization = 86
    return organization


#service
@pytest.fixture()
def service():
    service = "5fbdf757-7755-4e00-8520-93afcc72ca2e"
    return service


#author
@pytest.fixture()
def author():
    author = "c69d514a-08e0-437f-8d8e-e8dc67a9f409"
    return author


@pytest.fixture(scope='function')
def email():
    fake = Faker()
    return fake.email()


# @pytest.fixture()
# def natural_client(rand_first_name, rand_last_name, iin):
#    natural_client = {"first_name": rand_first_name, "last_name": rand_last_name, "iin": iin}
#    return natural_client


# @pytest.fixture()
# def client_identity_cards(document_type, number):
#     client_identity_cards = {"document_type": document_type, "number": number}
#     return client_identity_cards


@pytest.fixture()
def document_type():
    document_type = 1
    return document_type


# @pytest.fixture()
# def requisites(bank_id, bank, account_number):
#     requisites = {"bank_id": bank_id, "bank": bank, "account_number": account_number}
#     return requisites


@pytest.fixture()
def bank_id():
    bank_id = 1
    return bank_id


@pytest.fixture()
def bank():
    bank = "Kaspi Bank JSC"
    return bank


@pytest.fixture()
def account_number():
    account_number = "KZT123445678866H"
    return account_number


@pytest.fixture(scope='function')
def country():
    fake = Faker()
    return fake.country()


@pytest.fixture(scope='function')
def city():
    fake = Faker()
    return fake.city()


@pytest.fixture(scope='function')
def address():
    fake = Faker()
    return fake.street_address()


@pytest.fixture()
def number():
    return random.randint(0, 99999999)


@pytest.fixture()
def iin():
    return random.randint(0, 99999999999)


@pytest.fixture()
def referral():
    referral = "f2b93162-03a9-4558-9f75-df4ea7e3f0e7"
    return referral


@pytest.fixture()
def sex():
    sex = [1, 2]
    return random.choice(sex)


# @pytest.fixture()
# def client_phone(phone_number, comment):
#     client_phone = {"phone": phone_number, "comment": comment}
#     return client_phone


# managers
@pytest.fixture()
def managers():
    managers = ["c69d514a-08e0-437f-8d8e-e8dc67a9f409"]
    return managers


@pytest.fixture()
def notification_service():
    notification_service = "sms"
    print(notification_service)
    return notification_service


# @pytest.fixture()
# def get_random_request_id():
#     requests_list = ApiRequests().get_requests_list()
#     assert requests_list.status_code == 200
#     requests_list = requests_list.json()
#     requests_id = []
#     for i in requests_list['results']:
#         id_request = i['id']
#         requests_id.append(id_request)
#     requests_id.sort()
#     requests_id = random.choice(requests_id)
#     return requests_id


@pytest.fixture()
def print_ticket():
    print_ticket = 'true'
    print(print_ticket)
    return print_ticket


@pytest.fixture(scope='function')
def expire_at():
    expire_at = str(datetime.datetime.now())
    return expire_at
    # fake = Faker()
    # return fake.date()


@pytest.fixture(scope='function')
def birth_date():
    fake = Faker()
    return fake.date()


@pytest.fixture()
def is_individual_businessman():
    is_individual_businessman = [True, False]
    return random.choice(is_individual_businessman)


@pytest.fixture(scope='function')
def individual_company_name():
    fake = Faker()
    return fake.job()


@pytest.fixture()
def comment():
    comment = "test"
    return comment


@pytest.fixture()
def reason_pause():
    reason_pause = "08c59b49-bb97-4fb1-8f61-5ca8e651e2c0"
    return reason_pause


@pytest.fixture()
def reason_cancel():
    reason_cancel = "d47645cd-2391-4132-812a-e5cd0c8a4e09"
    return reason_cancel


@pytest.fixture(scope='function')
def get_id_requests():
    id_request = ApiRequests().get_requests_list()
    id_request = id_request.json()
    requests_id = []
    for i in id_request['results']:
        id_request = i['id']
        requests_id.append(id_request)
    requests_id.sort()
    last_request_id = [requests_id[-1]]
    print(last_request_id)
    return last_request_id


@pytest.fixture(scope="function")
def get_core_user():
    core_user_list = ApiCoreUser().get_core_user()
    core_user_list = core_user_list.json()
    core_list = []
    for i in core_user_list['results']:
        core_user_list = i['id']
        core_list.append(core_user_list)
    core_list.sort()
    last_core_id = core_list[-1]
    print(last_core_id)
    return last_core_id


@pytest.fixture(scope='function')
def test_post_natural_client(rand_first_name, rand_last_name, sex,
                             phone_number, comment
):
    client = ApiClients()
    response = client.get_client()

    assert response.status_code == 200

    if response.json()['count'] > 0:
        client_id = response.json()['results'][0]['id']
        return client_id


@pytest.fixture()
def password():
    password = "pass123"
    return password


@pytest.fixture()
def is_staff():
    is_staff = True
    return is_staff


@pytest.fixture()
def work_position():
    work_position = 15
    return work_position


@pytest.fixture()
def infosystems():
    infosystems = [4]
    return infosystems


@pytest.fixture()
def department():
    department = "324b4465-1bc3-44de-9a08-b0321b0ef229"
    return department


@pytest.fixture()
def position():
    positions = "ff2644bb-04ac-4085-8baa-b3dbfdf4b0f2"
    return positions


@pytest.fixture()
def is_active():
    is_active = True
    return is_active


@pytest.fixture()
def window(floor, place):
    window = {"floor": floor, "place": place}
    return window


@pytest.fixture()
def floor():
    floor = "1"
    return floor


@pytest.fixture()
def place():
    place = "1"
    return place


@pytest.fixture()
def status_poll():
    status_poll = 0
    return status_poll


@pytest.fixture()
def city():
    city = "Test"
    return city


@pytest.fixture()
def kind_poll():
    kind_poll = ["0", "10"]
    return random.choice(kind_poll)


@pytest.fixture()
def issue_at():
    issue_at = str(datetime.datetime.now())
    return issue_at


@pytest.fixture()
def autos(mark, model, vin_generate, year):
    autos = [{"mark": mark, "model": model, "vin": vin_generate, "year": year}]
    print(autos)
    return autos


@pytest.fixture()
def mark():
    return "hyundai"


@pytest.fixture()
def model():
    return "accent"


@pytest.fixture()
def vin_generate():
    wmi = "WMI" + str(random.randint(10000, 99999))
    vds = str(random.randint(100000, 999999))
    check_digit = str(random.randint(0, 9))
    vis = str(random.randint(100000, 999999))
    vin = wmi + vds + check_digit + vis
    return vin



@pytest.fixture()
def year():
    year = 2023
    return year


@pytest.fixture()
def manager_dms():
    manager_dms = "Test"
    return manager_dms


@pytest.fixture()
def client_id():
    client_id = 14000859
    return client_id

