from time import sleep

import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

"""
test cases for r7
"""
class FrontEndRestrictedUrlTest(BaseCase):
    def test_open_sell(self, *_):
        #R7.1.1
        # open logout page
        self.open(base_url + '/logout')
        # try to send a post request to sell
        r=requests.post(base_url+'/sell')
        #check that user is not given access
        #check user is still on login
        assert not r.is_redirect
        self.assert_equal(self.get_current_url(), base_url + '/login')
    def test_open_home(self, *_):
        #R7.1.1
        # open logout page
        self.open(base_url + '/logout')
        # try to open the homepage 
        self.open(base_url + '/')
        #check that user is not given access
        #check user is redirected to login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
    def test_open_buy(self, *_):
        #R7.1.1
        # open logout page
        self.open(base_url + '/logout')
        # try to send a post request to buy
        r=requests.post(base_url+'/sell')
        #check that user is not given access
        #check user is still on login
        assert not r.is_redirect
        self.assert_equal(self.get_current_url(), base_url + '/login')
    def test_open_update(self, *_):
        #R7.1.1
        # open logout page
        self.open(base_url + '/logout')
        # try to send a post request to update
        r=requests.post(base_url+'/sell')
        #check that user is not given access
        #check user is still on login
        assert not r.is_redirect
        self.assert_equal(self.get_current_url(), base_url + '/login')

