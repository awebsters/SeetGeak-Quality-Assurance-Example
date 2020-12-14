import pytest
from seleniumbase import BaseCase
from qa327.models import db, Ticket, User
from qa327_test.conftest import base_url
from werkzeug.security import generate_password_hash


@pytest.mark.usefixtures('server')
class PurchaseIntegrationTest(BaseCase):

    def setup(self):
        db.drop_all()
        db.create_all()

        # Create the state of the application to make it able to buy a ticket for a new user.
        # This allows the test to be independent from the ability to sell a ticket.
        # Remember this test is to test the full ability to create a user and buy a ticket not to sell one.
        owner = User(name="test", email="test_frontend@test.com", balance=5000,
                     password=generate_password_hash('Test1234!', method='sha256'))
        ticket = Ticket(name="Test", quantity=2, price=20, email="test_frontend@test.com")
        db.session.add(ticket)
        db.session.add(owner)
        db.session.commit()

    def register(self):

        """register new user"""
        self.open(base_url + '/logout')
        # Open register page
        self.open(base_url + '/register')
        # Fill out form

        self.type("#email", "test_integration@test.com")
        self.type("#name", "test2")
        self.type("#password", "Test1234!")
        self.type("#password2", "Test1234!")

        self.click('input[type="submit"]')

    def login(self):
        """ Login """
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_integration@test.com")
        self.type("#password", "Test1234!")
        # click enter button
        self.click('input[type="submit"]')

    def test_purchase_ticket(self):
        # Make new ticket
        self.setup()
        self.register()
        self.login()

        self.type("#buy-name", "Test")
        self.type("#buy-quantity", 1)

        self.click('input[value="Buy Ticket"]')

        self.assert_text("Test for $20 with 1 remaining, contact test_frontend@test.com", "#tickets > div:nth-child(1) > h4", timeout=15)