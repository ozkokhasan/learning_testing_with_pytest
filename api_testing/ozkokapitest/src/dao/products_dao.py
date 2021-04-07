from ozkokapitest.src.utilities.db_utilities import DBUtility
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, quantity=1):

        sql = 'SELECT * FROM local.wp_posts WHERE post_type = "product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(quantity))

    def get_product_by_id(self, product_id):

        sql = f'SELECT * FROM local.wp_posts WHERE ID = {product_id};'
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_products_created_after_given_date(self, _date):
        sql = f'SELECT * FROM local.wp_posts WHERE post_type = "product" AND post_date > "{_date}" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql
