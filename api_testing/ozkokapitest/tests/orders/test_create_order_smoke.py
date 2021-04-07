import pytest
from ozkokapitest.src.dao.products_dao import ProductsDAO
from ozkokapitest.src.helpers.orders_helper import OrdersHelper
from ozkokapitest.src.helpers.customers_helper import CustomerHelper

pytestmark = [pytest.mark.smoke, pytest.mark.orders]


@pytest.fixture(scope='module')
def my_setup():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()
    customer_helper = CustomerHelper()

    random_product = product_dao.get_random_product_from_db()
    product_id = random_product[0]['ID']

    info = {
        'product_id': product_id,
        'order_helper': order_helper,
        'customer_helper': customer_helper
    }

    return info


@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_setup):

    order_helper = my_setup['order_helper']

    customer_id = 0
    product_id = my_setup['product_id']

    # make the call
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ]
    }
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(
        order_json, customer_id, expected_products)


@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_setup):
    # helper objects
    order_helper = my_setup['order_helper']
    customer_helper = my_setup['customer_helper']

    product_id = my_setup['product_id']

    # make a new customer
    customer_info = customer_helper.create_customer()
    customer_id = customer_info['id']

    # make the call
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        "customer_id": customer_id}
    order_json = order_helper.create_order(additional_args=info)

    # verify response

    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(
        order_json, customer_id, expected_products)
