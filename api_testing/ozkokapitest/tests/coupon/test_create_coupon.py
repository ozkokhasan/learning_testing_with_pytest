import pytest
import random
from ozkokapitest.src.utilities.generic_utilities import generate_random_string
from ozkokapitest.src.utilities.woo_api_utility import WooApiUtility
from ozkokapitest.src.helpers.coupon_helper import CouponHelper
from ozkokapitest.src.dao.coupon_dao import CouponDAO

pytestmark = [pytest.mark.coupons]


@pytest.mark.parametrize("discount_type",
                         [
                             pytest.param(
                                 'percent', marks=pytest.mark.tcid37),
                             pytest.param(
                                 'fixed_cart', marks=pytest.mark.tcid38),
                             pytest.param(
                                 'fixed_product', marks=pytest.mark.tcid39),
                         ]
                         )
def test_create_coupon(discount_type):
    coupon_helper = CouponHelper()
    coupon_dao = CouponDAO()
    coupon_amount = random.randint(5, 21)
    generate_code = generate_random_string(
        length=10, prefix=(str(coupon_amount) + "off_"))

    # create the coupon
    info = {
        "code": generate_code,
        "discount_type": discount_type,
        "amount": str(coupon_amount)
    }
    coupon_json = coupon_helper.create_coupon(info)

    # verify the coupon in db
    coupon_in_db = coupon_dao.get_coupon_by_id(coupon_json['id'])
    coupon_meta_data = coupon_dao.get_coupon_meta_data(coupon_json['id'])

    assert coupon_in_db, f"Failed to insert coupon in database." \
        f"coupon_id: {coupon_json[id]}"

    # verify the discount_type and coupon amount in api and database

    assert coupon_meta_data[0]['meta_value'] == discount_type, \
        f"Failed to insert coupon 'discount_type' field. Incorrect discount_type. " \
        f"Expected: {discount_type} " \
        f"Actual: {coupon_meta_data[0]['meta_value']}"

    assert coupon_meta_data[1]['meta_value'] == str(coupon_amount), \
        f"Failed to insert coupon 'coupon_amount' field. Incorrect coupon_amount. " \
        f"Expected: {coupon_amount} "\
        f"Actuaş: {coupon_meta_data[1]['meta_value']}"


@pytest.mark.tcid40
def test_create_coupon_wwith_invalid_discount_type():
    discount_type = generate_random_string(length=10)
    coupon_helper = CouponHelper()
    coupon_dao = CouponDAO()
    coupon_amount = random.randint(5, 21)
    generate_code = generate_random_string(
        length=10, prefix=(str(coupon_amount) + "off_"))

    # create the coupon
    info = {
        "code": generate_code,
        "discount_type": discount_type,
        "amount": str(coupon_amount)
    }

    rs_api = WooApiUtility().post('coupons', params=info, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', \
        f"Post coupon status to random string did not have correct code in response." \
        f"Expected: 'rest_invalid_param'"\
        f"Actual: {rs_api['code']}"

    assert rs_api['message'] == 'Invalid parameter(s): discount_type', \
        f"Post coupon status to random string did not have correct message in response." \
        f"Expected: 'Invalid parameter(s): discount_type'"\
        f"Actual: {rs_api['message']}"
