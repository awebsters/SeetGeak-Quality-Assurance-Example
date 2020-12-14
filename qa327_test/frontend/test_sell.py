from time import sleep

import pytest
from seleniumbase import BaseCase


from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test1234!', method='sha256'),
    balance=5000
)


class SellPageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_name_space(self, *_):

        """
        R4.1.1 - Check that the name is only made up of numbers and letters, and is only allowed a space at the beginning or end

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')

        self.type("#name", "+")
        self.type("#quantity", 1)
        self.type("#price", 20)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))




        self.click('input[value="Sell Ticket"]')

        self.assert_text("Name can only contain alphanumeric characters", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_name_length(self, *_):
        """
        R4.2.1 - Check that the name is less than 60 characters long

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')



        self.type("#name", 6*"Teeeeeeeeest")
        self.type("#quantity", 1)
        self.type("#price", 20)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

        self.assert_text("Name is too long, it must be shorter than 60 characters", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_quantity_range_lower(self, *_):
        """
        R4.3.1 - Check failure for quantity of 0

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')

        self.type("#name", "Test")
        self.type("#quantity", 0)
        self.type("#price", 20)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

        self.assert_text("Quantity must be greater than 0 and less than or equal to 100", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_quantity_range_upper(self, *_):
        """
        R4.3.2 - Check failure for quantity of 101

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')

        self.type("#name", "Test")
        self.type("#quantity", 101)
        self.type("#price", 20)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

        self.assert_text("Quantity must be greater than 0 and less than or equal to 100", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_price_range_lower(self, *_):
        """
        R4.4.1 - Check failure for range < 10

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')

        self.type("#name", "Test")
        self.type("#quantity", 1)
        self.type("#price", 9)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

        self.assert_text("Price must be greater than or equal to 10 and less than or equal to 100", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_price_range_upper(self, *_):
        """
        R4.4.2 - Check failure for range > 100

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')

        self.type("#name", "Test")
        self.type("#quantity", 1)
        self.type("#price", 101)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

        self.assert_text("Price must be greater than or equal to 10 and less than or equal to 100", "#message")


    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_ticket_user_profile(self, *_):
        """
        R4.5.1 - Check Success for date in correct format

        """
        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open login page
        self.open(base_url + '/login')
        # Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')

        self.type("#name", "Test")
        self.type("#quantity", 1)
        self.type("#price", 20)
        self.execute_script("document.querySelector('#date').setAttribute('value', '{}')".format('2020-09-01'))

        self.click('input[value="Sell Ticket"]')

