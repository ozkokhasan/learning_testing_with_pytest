import pymysql
import logging as logger
import os
from ozkokapitest.src.utilities.credentials_utilities import CredentialsUtility
from ozkokapitest.src.configs.hosts_config import DB_HOSTS


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.machine = os.environ.get('MACHINE')
        assert self.machine, f"Environment variable 'MACHINE' must be set!"

        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, f"Environment variable 'WP_HOST' must be set!"

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f"Can not run test in docker if WP_HOST=local")

        self.env = os.environ.get('ENV', 'test')

        self.creds = creds_helper.get_db_credentials()
        self.host = DB_HOSTS[self.machine][self.env]['host']
        self.port = DB_HOSTS[self.machine][self.env]['port']
        self.database = DB_HOSTS[self.machine][self.env]['database']
        self.table_prefis = DB_HOSTS[self.machine][self.env]['table_prefix']

    def create_connection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.creds['db_user'],
            password=self.creds['db_password'],
            port=self.port
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
