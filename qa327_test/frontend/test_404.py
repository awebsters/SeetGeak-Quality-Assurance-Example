import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


class PageNotFoundTest(BaseCase):

    def test_404_page_open(self, *_):
        # open non-existant page
        self.open(base_url + "/test")
        # make sure 404 error is displayed
        self.assert_element("#message")
        self.assert_text("Sorry we couldn't find the page you're looking fo", "#message")
        self.assert_element("#header")
        self.assert_text("404 error", "#header")

