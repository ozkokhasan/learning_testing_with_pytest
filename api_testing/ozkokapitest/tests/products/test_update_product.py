import pytest
from ozkokapitest.src.utilities.generic_utilities import generate_random_string
from ozkokapitest.src.helpers.product_helper import ProductsHelper

pytestmark = [pytest.mark.products]


@pytest.mark.tcid61
def test_update_product_regular_price():

    # create a product
    product_helper = ProductsHelper()
    payload = {}
    payload['name'] = generate_random_string(length=20, prefix="test_")
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"
    product_json = product_helper.call_create_product(payload)
    product_id = product_json['id']

    # update a product price
    updated_data = {"regular_price": "25.99"}
    rs_api = product_helper.call_update_an_product(product_id, updated_data)

    # verify the response
    assert rs_api['regular_price'] == updated_data['regular_price'], \
        f"Update a product 'regular_price' field is failed." \
        f"Expected: {updated_data['regular_price']}" \
        f"Actual: {rs_api['regular_price']}"


@pytest.mark.tcid63
def test_update_product_on_sale():

    # create a product
    product_helper = ProductsHelper()
    payload = {}
    payload['name'] = generate_random_string(length=20, prefix="test_")
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"
    product_json = product_helper.call_create_product(payload)
    product_id = product_json['id']

    assert not product_json[
        'on_sale'], f"Newly created product should not have 'on_sale=True'. Product id: {product_id}"
    assert not product_json['sale_price'], f"Newly created product should not have value for 'sale_price' field."

    # update a product sale_price field > 0
    product_helper.call_update_an_product(product_id, {'sale_price': '8.99'})
    product_after_update = product_helper.get_product_by_id(product_id)
    assert product_after_update['sale_price'] == '8.99', \
        f"Updating 'sale_price' field failed." \
        f"Expected value: 8.99 ." \
        f"Actual value: {product_after_update['sale_price']}"

    # validating on_sale field = True
    assert product_after_update['on_sale'], \
        f"Updated 'sale_price' of product, but the 'on_sale' did not set to 'True'." \
        f"Product id: {product_id}"

    # update a product sale_price field = ''
    product_helper.call_update_an_product(product_id, {'sale_price': ''})
    product_after_update = product_helper.get_product_by_id(product_id)

    # validating on_sale field = False
    assert not product_after_update['on_sale'], \
        f"Updated 'sale_price=""' of product, but the 'on_sale' did not set to 'False'." \
        f"Product id: {product_id}"
