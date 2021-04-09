from ozkokapitest.src.utilities.db_utilities import DBUtility


class CouponDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_coupon_by_id(self, coupon_id):
        sql = f'SELECT * FROM local.wp_posts WHERE ID = {coupon_id};'

        return self.db_helper.execute_select(sql)

    def get_coupon_meta_data(self, coupon_id):
        sql = f'SELECT * FROM local.wp_postmeta WHERE post_id = {coupon_id};'

        return self.db_helper.execute_select(sql)
