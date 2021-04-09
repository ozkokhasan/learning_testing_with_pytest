from ozkokapitest.src.utilities.woo_api_utility import WooApiUtility


class CouponHelper(object):

    def __init__(self):
        self.woo_helper = WooApiUtility()

    def create_coupon(self, payload):
        rs_api = self.woo_helper.post(
            'coupons', params=payload, expected_status_code=201)

        return rs_api
