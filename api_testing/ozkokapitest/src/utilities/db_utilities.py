import pymysql
import logging as logger
from ozkokapitest.src.utilities.credentials_utilities import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.creds['db_user'],
            password=self.creds['db_password'],
            port=10005
        )
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql}. Error: {str(e)}")
        finally:
            conn.close()
        return rs_dict

    def execute_sql(self, sql):
        pass
