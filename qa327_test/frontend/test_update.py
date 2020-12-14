from time import sleep

import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend', method='sha256')
)


class UpdatePageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def login(self, *_):
        self.open(base_url + '/login')
        # fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", 'Test_frontend')
        # submit
        self.click('input[type="submit"]')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_invalid_name(self, *_):
        """
        R5.1.1
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)

        # enter in update form information
        self.type("#update-name","*hi^xd!")
        self.type("#update-quantity", 1)
        self.type("#update-price", 15)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Name can only contain alphanumeric characters", '#update-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_invalid_name_space(self, *_):
        """
        R5.1.2
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name"," ohno")
        self.type("#update-quantity", 1)
        self.type("#update-price", 15)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Name has space at beginning or end", '#update-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_name_length(self, *_):
        """
        R5.2.1
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name","imtoolong"*7)
        self.type("#update-quantity", 1)
        self.type("#update-price", 15)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Name is too long, it must be shorter than 60 characters", "#update-message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_quantity_range_high(self, *_):
        """
        R5.3.1
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name","Test123")
        self.type("#update-quantity", 101)
        self.type("#update-price", 15)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Quantity must be greater than 0 and less than or equal to 100", "#update-message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_quantity_range_low(self, *_):
        """
        R5.3.2
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name","Test123")
        self.type("#update-quantity", 0)
        self.type("#update-price", 15)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Quantity must be greater than 0 and less than or equal to 100", "#update-message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_price_range_low(self, *_):
        """
        R5.4.1
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name","Test123")
        self.type("#update-quantity", 2)
        self.type("#update-price", 5)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Price must be greater than or equal to 10 and less than or equal to 100", "#update-message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_price_range_high(self, *_):
        """
        R5.4.2
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name","Test123")
        self.type("#update-quantity", 2)
        self.type("#update-price", 105)
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        self.click('input[value="Update Ticket"]')

        self.assert_text("Price must be greater than or equal to 10 and less than or equal to 100", "#update-message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_user_profile(self, *_):
        """
        R5.5.1
        """
        # invalidate any logged in sessions
        self.open(base_url + '/logout')
        # open login page
        self.login()
        # open home page
        self.open(base_url)
        # enter in update form information
        self.type("#update-name","Test123")
        self.type("#update-quantity", 2)
        self.type("#update-price", 15)
        # valid date format
        self.execute_script("document.querySelector('#update-date').setAttribute('value', '{}')".format('2020-12-10'))

        # successfully update ticket
        self.click('input[value="Update Ticket"]')

