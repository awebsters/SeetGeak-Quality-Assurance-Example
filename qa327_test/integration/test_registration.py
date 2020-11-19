import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class Registered(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test@gmail.com")
        self.type("#name", "test")
        self.type("#password", "Test0!")
        self.type("#password2", "Test0!")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test@gmail.com")
        self.type("#password", "Test0!")
        self.click('input[type="submit"]')

    def test_register_login(self):
        """ This test checks the implemented login/logout feature """
        self.register()
        self.login()
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Hi test", "#welcome-header")
