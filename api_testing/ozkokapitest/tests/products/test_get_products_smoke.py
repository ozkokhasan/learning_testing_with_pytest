import pytest
from ozkokapitest.src.utilities.request_utilities import RequestUtility
from ozkokapitest.src.dao.products_dao import ProductsDAO
from ozkokapitest.src.helpers.product_helper import ProductsHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    req_hellper = RequestUtility()
    rs_api = req_hellper.get('products')

    assert rs_api, f"Response of list all products empty"


@pytest.mark.tcid25
def test_get_product_by_id():

    # get product from db
    product_dao = ProductsDAO()
    random_product = product_dao.get_random_product_from_db()
    random_product_id = random_product[0]['ID']

    # make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(random_product_id)

    # verify the response
    assert random_product[0]['post_title'] == rs_api['name'], \
        f"Get product by id returned wrond product." \
        f"Id: {random_product_id}" \
        f"DB name: {random_product[0]['post_title']}" \
        f"API name: {rs_api['name']}"
