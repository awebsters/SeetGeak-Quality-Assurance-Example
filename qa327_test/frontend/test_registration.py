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



class RegistrationPageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_login_redirect(self, *_):
        """
        R2.1.1 - Tests if the homepage will redirect to / with a valid session

        """


        #Invalidate any logged in sessions
        self.open(base_url + '/logout')
        #Open login page
        self.open(base_url + '/login')
        #Fill in form
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test1234!")
        # Submit
        self.click('input[type="submit"]')
        sleep(2)
        # Open register page
        self.open(base_url + '/register')
        sleep(2)
        self.assert_equal(self.get_current_url(), base_url + '/')

    def test_login_not_redirect(self, *_):
        """
        R2.2.1 - Tests if it will stay on /register with no session

        """
        #Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')

        self.assert_equal(self.get_current_url(), base_url + '/register')

    def test_registration_form_present(self, *_):
        """
        R2.3.1- Tests if the /register page has input fields for email, username password and password2

        """
        #Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        #Check if elements exist
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")

    def test_registration_POST_request(self, *_):
        """
        R2.4.1- Check if a valid POST request can be submited to /register page and confirm success

        """
        #Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        #Check if post can be sent to

    @patch('qa327.backend.get_user', return_value=None)
    @patch('qa327.backend.register_user', return_value=True)
    def test_registration_valid_input(self, *_):
        """
        R2.5.1- Check success with all valid inputs
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        #Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.assert_equal(self.get_current_url(), base_url + '/login')

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_invalid_email_input(self, *_):
        """
        R2.5.2- Check failure with only email as invalid
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test")
        self.type("#name", "test")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.assert_text("Email format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_invalid_password_length_input(self, *_):
        """
        R2.5.3- Check failure with password length < 6
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "T")
        self.type("#password2", "T")

        self.click('input[type="submit"]')


        self.assert_text("Password format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_invalid_password_uppercare_input(self, *_):
        """
        R2.5.4- Check failure with password with no uppercase letters
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "test1234!")
        self.type("#password2", "test1234!")

        self.click('input[type="submit"]')


        self.assert_text("Password format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_invalid_password_lowercase_input(self, *_):
        """
        R2.5.5- Check failure with password with no lowercase letters
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "TEST1234!")
        self.type("#password2", "TEST1234!")

        self.click('input[type="submit"]')


        self.assert_text("Password format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_invalid_password_NoSpecialCharacters_input(self, *_):
        """
        R2.5.6- Check failure with password with no special characters
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "Test1234")
        self.type("#password2", "Test1234")

        self.click('input[type="submit"]')

        self.assert_text("Password format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_passwords_dont_match(self, *_):
        """
        R2.6- Check registration failure if password2 != password
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!!")

        self.click('input[type="submit"]')

        self.assert_text("The passwords do not match", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_empty_name(self, *_):
        """
        R2.7.1- Check failure with empty username
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.assert_equal(self.get_current_url(), base_url + '/register')

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_username_non_alphanumeric(self, *_):
        """
        R2.7.2- check failure with a non-alphanumeric character
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test!")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.wait_for_element("#message")

        self.assert_text("Name format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_username_invalid_space(self, *_):
        """
        R2.7.4- Check failure with a space at the end
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test ")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')


        self.assert_text("Name format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_username_invalid_length2(self, *_):
        """
        R2.8.1- Check failure with username of length 2
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Te")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.assert_text("Name format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    def test_registration_username_invalid_length20(self, *_):
        """
        R2.8.2- Check failure with username of length 20
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Teeeeeeeeeeeeeeeeeessst")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.assert_text("Name format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_registration_email_exists(self, *_):
        """
        R2.8.2- Check failure with username of length 20
        """

        # Invalidate any logged in sessions
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

        self.assert_text("This email has been ALREADY used", "#message")

