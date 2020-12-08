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
    password=generate_password_hash('Test_frontend', method='sha256'),
    balance=5000
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '1000', 'quantity': 5, 'email': 'test_frontend@test.com'},
    {'name': 't2', 'price': '10', 'quantity': 5, 'email': 'test_frontend@test.com'}
]

class FrontEndBuyTest(BaseCase):

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
    def test_buy_invalid_name(self, *_):
        """
        R6.1.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name","*_%^")
        self.type("#buy-quantity","1")
        self.click('#buy-btn-submit')
        self.assert_text("Name can only contain alphanumeric characters", '#buy-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_name_space(self, *_):
        """
        R6.1.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name"," t1")
        self.type("#buy-quantity","1")
        self.click('#buy-btn-submit')
        self.assert_text("Name has space at beginning or end", '#buy-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_name_length(self, *_):
        """
        R6.2.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name","ababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
        self.type("#buy-quantity","1")
        self.click('#buy-btn-submit')
        self.assert_text("Name is too long, it must be shorter than 60 characters", '#buy-message')
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_quantity_nan(self, *_):
        """
        R6.3.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name","t1")
        self.type("#buy-quantity","a")
        self.click('#buy-btn-submit')
        self.assert_text("Quantity must be a number", '#buy-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_quantity_negative(self, *_):
        """
        R6.3.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name","t1")
        self.type("#buy-quantity","0")
        self.click('#buy-btn-submit')
        self.assert_text("Quantity must be greater than 0 and less than or equal to 100", '#buy-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_quantity_100(self, *_):
        """
        R6.3.2
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name"," t1")
        self.type("#buy-quantity","101")
        self.click('#buy-btn-submit')
        self.assert_text("Quantity must be greater than 0 and less than or equal to 100", '#buy-message')    

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_quantity_large(self, *_):
        """
        R6.4.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name"," t1")
        self.type("#buy-quantity","6")
        self.click('#buy-btn-submit')
        self.assert_text("Ticket could not be bought", '#buy-message') 

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy_invalid_balance(self, *_):
        """
        R6.5.1
        """
        self.login()
        # open home page
        self.open(base_url)
        # enter in buy information
        self.type("#buy-name"," t1")
        self.type("#buy-quantity","5")
        self.click('#buy-btn-submit')
        self.assert_text("Ticket could not be bought", '#buy-message') 