import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]


@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")

    return {'id': 20, 'name': 'Hasan'}


@pytest.mark.smoke
def test_login_page_valid_user(my_setup):
    print("Login with valid user")
    print("Function: aaaaaa")
    print("id: {}".format(my_setup.get('id')))


@pytest.mark.regression
def test_loogin_page_wrong_password(my_setup):
    print("Login with wrong password")
    print("Function: bbbbbb")
    print("name: {}".format(my_setup.get('name')))
    # assert 1 == 2, 'One is not Two'
