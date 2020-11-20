import pytest
from seleniumbase import BaseCase



class PageNotFoundTest(BaseCase):

    def test_404_page_open(self, *_):
        #R8.1.1
        # open non-existant page
        self.open(base_url + "/test")
        # make sure 404 error is displayed
        self.assert_element("#message")
        self.assert_text("Sorry we couldn't find the page you're looking fo", "#message")
        self.assert_element("#header")
        self.assert_text("404 error", "#header")

