import pytest
from ozkokapitest.src.utilities.request_utilities import RequestUtility


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customer():

    req_hellper = RequestUtility()
    rs_api = req_hellper.get('customers')

    assert rs_api, f"Response of list all customers is empty"
