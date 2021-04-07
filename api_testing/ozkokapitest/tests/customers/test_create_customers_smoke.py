import pytest
import logging as logger
from ozkokapitest.src.utilities.generic_utilities import generate_random_email_and_password
from ozkokapitest.src.helpers.customers_helper import CustomerHelper
from ozkokapitest.src.dao.customer_dao import CustomerDAO
from ozkokapitest.src.utilities.request_utilities import RequestUtility


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    customer = CustomerHelper()
    customer_api_info = customer.create_customer(
        email=email, password=password)

    # verify email and first name in the response
    assert customer_api_info[
        'email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert customer_api_info['first_name'] == '', f"Create customer api returned value for firs_name but it should be empty."

    # verify customer is created in database
    cust_dao = CustomerDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = customer_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database.' \
                                  f'Email: {email}'


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    # get existing email from db
    customer_dao = CustomerDAO()
    existing_customer = customer_dao.get_random_customer_from_db()
    existing_email = existing_customer[0]['user_email']

    # make the call
    request_helper = RequestUtility()
    payload = {"email": existing_email, "password": "Password1"}

    customer_api_info = request_helper.post(
        endpoint='customers',
        payload=payload,
        expected_status_code=400
    )

    assert customer_api_info['code'] == 'registration-error-email-exists', \
        f"Create customer with existing user error 'code' is not correct." \
        f"Expected: 'registration-error-email-exists' Actual: {customer_api_info['code']}"

    assert customer_api_info['message'] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>', \
        f"Create customer with existing user error 'message' is not correct." \
        f'Expected: "An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>"' \
        f"Actual: {customer_api_info['message']}"
