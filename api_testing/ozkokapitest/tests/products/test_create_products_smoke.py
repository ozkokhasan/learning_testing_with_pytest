from ozkokapitest.src.utilities.generic_utilities import generate_random_string
from ozkokapitest.src.helpers.product_helper import ProductsHelper
from ozkokapitest.src.dao.products_dao import ProductsDAO
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid26
def test_create_simple_product():

    # generate data
    payload = {}
    payload['name'] = generate_random_string(length=20, prefix="test_")
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create product api response is empty." \
        f"Payload: {payload}"
    assert product_rs['name'] == payload['name'], \
        f"Create product api call response has unexpected name." \
        f"Expected: {payload['name']}, Actual: {product_rs['name']}"

    # verify the product exists in DB
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], \
        f"Create product, title in db does not match." \
        f"DB: {db_product['post_title']} API: {payload['name']}"
