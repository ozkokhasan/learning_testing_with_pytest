import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.mark.smoke
class TestCheckout(object):

    def test_checkout_as_guest(self):
        print("checkout as guest")
        print("Class: 1111111111")

    def test_checkout_with_existing_acount(self):
        print("checkout with existing acount")
        print("Class: 2222222222")
