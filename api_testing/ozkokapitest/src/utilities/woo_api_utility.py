import os
import logging as logger
from ozkokapitest.src.configs.hosts_config import WOO_API_HOSTS
from ozkokapitest.src.utilities.credentials_utilities import CredentialsUtility
from woocommerce import API


class WooApiUtility(object):

    def __init__(self):

        wc_creeds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]
        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creeds['wc_key'],
            consumer_secret=wc_creeds['wc_secret'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f"Bad Status code." \
            f"Expected: {self.expected_status_code}" \
            f"Actual: {self.status_code}" \
            f"URL: {self.base_url}" \
            f"Response Json: {self.rs_json}"

    def get(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.post(wc_endpoint, data=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

    def put(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.put(wc_endpoint, data=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json
