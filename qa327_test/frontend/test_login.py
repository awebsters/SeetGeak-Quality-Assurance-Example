import pytest
import requests
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

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


class FrontEndLoginPageTest(BaseCase):

    def test_login_page(self, *_):
        #R1.1
        self.open(base_url+'/logout')
        # open base page
        r=requests.get(base_url+'/login')
        assert not r.is_redirect
    def test_login_post_empty(self, *_):
        #R1.5.1
        self.open(base_url+'/logout')
        # open base page
        r=requests.post(base_url+'/login',{'email':'','password':''})
        assert not r.is_redirect
    def test_login_message(self, *_):
        #R1.2
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_submit(self, *_):
        #R1.10.1
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_no_error(self, *_):
        #R1.7.1
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_text_not_visible("email/password format incorrect","#message")
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_email_no_at(self, *_):
        #R1.7.2
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "test_frontend.com")
        self.type("#password", "Test1234!'")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password format invalid", "#message")
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_email_no_dot(self, *_):
        #R1.7.2
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "test@frontendcom")
        self.type("#password", "Test1234!'")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password format invalid", "#message")
    def test_login_elements(self, *_):
        #R1.4
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
        self.assert_element("#email")
        self.assert_element("#password")
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_empty_password(self, *_):
        #R1.6.2
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "test_frontend@test.com")
        # click enter button
        self.click('input[type="submit"]')
        errorMessage = self.get_attribute("#password", "required")
        self.assert_true(errorMessage)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_empty_email(self, *_):
        #R1.6.1
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill  password
        self.type("#password", "Test1234!'")
        # click enter button
        self.click('input[type="submit"]')
        errorMessage = self.get_attribute("#password", "required")
        self.assert_true(errorMessage)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_empty_elements(self, *_):
        #R1.6.3
        self.open(base_url+'/logout')
        # open login page
        self.open(base_url + '/login')
        # click enter button
        self.click('input[type="submit"]')
        passErrorMessage = self.get_attribute("#password", "required")
        emailErrorMessage = self.get_attribute("#email", "required")
        self.assert_true(passErrorMessage)
        self.assert_true(emailErrorMessage)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_invalid_pass_length(self, *_):
        #R1.8.1
        self.open(base_url+'/logout')
        # open login page
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password","12AB!")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password format invalid", "#message")
    def test_login_invalid_pass_no_lower(self, *_):
        #R1.8.3
        self.open(base_url+'/logout')
        # open login page
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password","123456A!")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password format invalid", "#message")
    def test_login_invalid_pass_no_upper(self, *_):
        #R1.8.2
        self.open(base_url+'/logout')
        # open login page
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password","123456a!")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password format invalid", "#message")  
    def test_login_invalid_pass_no_special_character(self, *_):
        #R1.8.4
        self.open(base_url+'/logout')
        # open login page
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password","123456Aa")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password format invalid", "#message")  
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_redirect(self, *_):
        #R1.3.1
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/login')
        self.assert_element("#welcome-header")
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_invalid_combo(self, *_):
        #R1.11.1
        self.open(base_url+'/logout')
        # open base page
        self.open(base_url + '/login')
         # fill email and password
        self.type("#email", "tesgfdgf123@test.com")
        self.type("#password", "Tesgggggg5dr234!")
        # click enter button
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("email/password combination incorrect", "#message")