import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.mark.smoke
def test_login_page_valid_user():
    print("Login with valid user")
    print("Function: aaaaaa")


@pytest.mark.regression
def test_loogin_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbbb")
    # assert 1 == 2, 'One is not Two'
