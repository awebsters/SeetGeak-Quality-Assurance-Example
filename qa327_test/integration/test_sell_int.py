import pytest
from seleniumbase import BaseCase
from qa327.models import db
from qa327_test.conftest import base_url



@pytest.mark.usefixtures('server')
class Sell(BaseCase):

    def setup(self):
        db.drop_all()
        db.create_all()


    def register(self):

        """register new user"""
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

    def login(self):
        """ Login """
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # click enter button
        self.click('input[type="submit"]')

    def test_make_ticket(self):
        # Make new ticket
        self.setup()
        self.register()
        self.login()

        self.type("#name", "Test")
        self.type("#quantity", 1)
        self.type("#price", 20)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

        self.assert_text("Test for $20 with 1 remaining, contact test_frontend@test.com", "#tickets > div:nth-child(1) > h4")



