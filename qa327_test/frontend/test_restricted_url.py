from time import sleep

import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
test cases for r7
"""
class FrontEndRestrictedUrlTest(BaseCase):
    def test_open_sell(self, *_):
        # open logout page
        self.open(base_url + '/logout')
        # try to open sell
        self.open(base_url + '/sell')
        #check that user is not given access
        #check user is redirected to login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    def test_open_home(self, *_):
        # open logout page
        self.open(base_url + '/logout')
        # try to open the homepage 
        self.open(base_url + '/')
        #check that user is not given access
        #check user is redirected to login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    def test_open_buy(self, *_):
        # open logout page
        self.open(base_url + '/logout')
        # try to open buy
        self.open(base_url + '/buy')
        #check that user is not given access
        #check user is redirected to login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    def test_open_update(self, *_):
        # open logout page
        self.open(base_url + '/logout')
        # try to open update
        self.open(base_url + '/update')
        #check that user is not given access
        #check user is redirected to login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

