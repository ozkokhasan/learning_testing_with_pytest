import pytest
from ozkokapitest.src.helpers.orders_helper import OrdersHelper
from ozkokapitest.src.utilities.woo_api_utility import WooApiUtility
from ozkokapitest.src.utilities.generic_utilities import generate_random_string

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.parametrize("new_status",
                         [
                             pytest.param(
                                 'cancelled', marks=pytest.mark.tcid55),
                             pytest.param(
                                 'completed', marks=pytest.mark.tcid56),
                             pytest.param(
                                 'on-hold', marks=pytest.mark.tcid57),
                         ]
                         )
def test_update_order_status(new_status):

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    current_status = order_json['status']
    assert current_status != new_status, \
        f"Current status of order is already {new_status}" \
        f"Unable to run test."

    # update status
    order_id = order_json['id']
    payload = {
        "status": new_status
    }
    order_helper.call_update_an_order(order_id, payload)

    # get order information and verify
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    assert new_order_info['status'] == new_status, \
        f"Updated order status to '{new_status}'," \
        f"but order status is still {new_order_info['status']}"


@pytest.mark.tcid58
def test_update_order_status_to_random_string():

    new_status = 'test_abcd'

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    current_status = order_json['status']
    order_id = order_json['id']

    # update status
    payload = {
        "status": new_status
    }

    rs_api = WooApiUtility().put(
        f'orders/{order_id}', params=payload, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', \
        f"Update order status to random string did not have correct code in response." \
        f"Expected: 'rest_invalid_param'"\
        f"Actual: {rs_api['code']}"

    assert rs_api['message'] == 'Invalid parameter(s): status', \
        f"Update order status to random string did not have correct message in response." \
        f"Expected: 'Invalid parameter(s): status'"\
        f"Actual: {rs_api['message']}"


@pytest.mark.tcid59
def test_update_order_customer_note():

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update customer_note
    random_string = generate_random_string(40)
    payload = {
        "customer_note": random_string}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    assert new_order_info['customer_note'] == random_string, \
        f"Update order's 'customer_note' field failed." \
        f"Expected: {random_string} " \
        f"Actual: {new_order_info['customer_note']}"
