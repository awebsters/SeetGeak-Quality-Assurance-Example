import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.

The tests will only test the frontend portion of the program, by patching the backend to return
specific values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend', method='sha256'),
    balance=5000
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'quantity': 5, 'email': 'test_frontend@test.com'},
    {'name': 't2', 'price': '100', 'quantity': 5, 'email': 'test_frontend@test.com'}
]


class FrontEndHomePageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def login(self, *_):
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", "Test_frontend")
        # click enter button
        self.click('input[type="submit"]')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_redirect(self, *_):
        """
        R3.1.1 - This tests if the homepage will redirect to the login page
        without a user loggedin
        """
        # open home page
        self.open(base_url + '/logout')
        self.open(base_url)

        self.assert_equal(self.get_current_url(), base_url + '/login')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_header(self, *_):
        """
        R3.2.1 - This tests if the homepage properly displays the username in the
        #welcome-header
        """

        self.login()

        # open home page
        self.open(base_url)

        self.assert_text("Hi {}".format(test_user.name), '#welcome-header')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_balance(self, *_):
        """
        R3.3.1 - This tests if the homepage properly displays the balance
        """
        # open home page

        self.login()

        self.open(base_url)

        self.assert_text("Balance: {}".format(test_user.balance), '#balance h4')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_logout_link(self, *_):
        """
        R3.4.1 - This tests if their is a logout link
        """
        self.login()

        # open home page
        self.open(base_url)

        # Assert an anchor tag exists that goes to the logout route
        self.assert_element_present('a[href*="/logout"]')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_ticket_list(self, *_):
        """
        R3.5.1 - This tests if tickets are displayed
        """
        self.login()

        # open home page
        self.open(base_url)

        # Create a string of tickets that should be displayed
        string = ''
        for ticket in test_tickets:
            string += '{} for ${} with {} remaining, contact {}\n'.format(ticket['name'], ticket['price'],
                                                                        ticket['quantity'], ticket['email'])
        # We have an extra newline character, remove it
        string = string.rstrip('\n')
        self.assert_text(string, '#tickets')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_sell_form_exists(self, *_):
        """
        R3.6.1 - This tests if the ticket selling form exists
        and contains the correct fields.
        """
        self.login()

        # open home page
        self.open(base_url)

        # make sure each field exists under a form with the action to sell
        self.assert_element_present('form[action*="/sell"] #name')
        self.assert_element_present('form[action*="/sell"] #quantity')
        self.assert_element_present('form[action*="/sell"] #price')
        self.assert_element_present('form[action*="/sell"] #date')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_buy_form_exists(self, *_):
        """
        R3.7.1 - This tests if the ticket buying form exists
        and contains the correct fields.
        """
        self.login()

        # open home page
        self.open(base_url)

        # make sure each field exists under a form with the action to buy
        self.assert_element_present('form[action*="/buy"] #buy-name')
        self.assert_element_present('form[action*="/buy"] #buy-quantity')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_update_form_exists(self, *_):
        """
        R3.8.1 - This tests if the ticket update form exists
        and contains the correct fields.
        """
        self.login()

        # open home page
        self.open(base_url)

        # make sure each field exists under a form with the action to update
        self.assert_element_present('form[action*="/update"] #update-name')
        self.assert_element_present('form[action*="/update"] #update-quantity')
        self.assert_element_present('form[action*="/update"] #update-price')
        self.assert_element_present('form[action*="/update"] #update-date')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.create_ticket', return_value=None)
    def test_home_sell_form(self, *_):
        """
        R3.9.1 - This tests if the ticket selling form can be submitted
        """
        self.login()

        # open home page
        self.open(base_url)

        # Click the sell form button
        self.click('form[action*="/sell"] input[type="submit"]')

        # If the form does not go anywhere and POST correctly we will see a 404 error page
        self.assert_text_not_visible("404 error")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_buy_form(self, *_):
        """
        R3.10.1 - This tests if the ticket buying form can be submitted
        """
        self.login()

        # open home page
        self.open(base_url)

        # Click the buy form button
        self.click('form[action*="/buy"] input[type="submit"]')

        # If the form does not go anywhere and POST correctly we will see a 404 error page
        self.assert_text_not_visible("404 error")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_home_update_form(self, *_):
        """
        R3.11.1 - This tests if the ticket update form can be submitted
        """
        self.login()

        # open home page
        self.open(base_url)

        # Click the update form button
        self.click('form[action*="/update"] input[type="submit"]')

        # If the form does not go anywhere and POST correctly we will see a 404 error page
        self.assert_text_not_visible("404 error")
