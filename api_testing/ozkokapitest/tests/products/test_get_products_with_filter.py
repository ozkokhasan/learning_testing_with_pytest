import pytest
from datetime import datetime, timedelta
from ozkokapitest.src.helpers.product_helper import ProductsHelper
from ozkokapitest.src.dao.products_dao import ProductsDAO


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        # create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - \
            timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()
        payload = {}
        payload['after'] = after_created_date

        # make the call
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, f"Empty response for list products with filter"

        # get data from db
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        # verify response matches db
        assert len(rs_api) == len(db_products), \
            f"List of products with filter 'after' returned unexpected number of products." \
            f"Expected: {len(db_products)}, Actual: {len(rs_api)}"

        # verify ids
        ids_in_api = [element['id'] for element in rs_api]
        ids_in_db = [element['ID'] for element in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List products with filter." \
            f"Product ids in response mismatch in db."
