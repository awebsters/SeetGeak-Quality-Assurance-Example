from unittest.mock import patch
from unittest import TestCase
from qa327.models import db, User, Ticket
import qa327.backend as bn
from werkzeug.security import generate_password_hash, check_password_hash


class BackEndBuyTicketTest(TestCase):
    '''
    This tests the backend function Buy Tickets.
    The Analysis can be found at 'qa327_test/test_backend_specification/Buy_Ticket.md'
    '''

    test_user = User(
        email='test_backend_owner@test.com',
        name='test_backend_owner',
        password=generate_password_hash('Test_backend_owner', method='sha256'),
        balance=0
    )
    test_user_2 = User(
        email='test_backend@test.com',
        name='test_backend',
        password=generate_password_hash('Test_backend', method='sha256'),
        balance=5000
    )
    invalid_user = User(
        email='test_invalid@test.com',
        name='test_invalid',
        password=generate_password_hash('Test_invalid', method='sha256'),
    )
    test_ticket = Ticket(
        name='t1',
        price=50.0,
        quantity=100,
        email='test_backend_owner@test.com'
    )
    test_ticket_invalid_user = Ticket(
        name='t2',
        price=50.0,
        quantity=100,
        email='test_invalid@test.com'
    )

    @classmethod
    def setUpClass(cls):
        '''
        This gets run before all test cases in this class
        Use this method to make any database changes you need before running the
        backend code
        '''

        # Remove objects before we insert fresh ones
        if User.query.filter_by(email=cls.test_user.email).first():
            db.session.delete(BackEndBuyTicketTest.test_user)
        if User.query.filter_by(email=cls.test_user_2.email).first():
            db.session.delete(BackEndBuyTicketTest.test_user_2)
        if User.query.filter_by(email=cls.invalid_user.email).first():
            db.session.delete(BackEndBuyTicketTest.invalid_user)

        if Ticket.query.filter_by(name=cls.test_ticket.name).first():
            db.session.delete(BackEndBuyTicketTest.test_ticket)
        if Ticket.query.filter_by(name=cls.test_ticket_invalid_user.name).first():
            db.session.delete(BackEndBuyTicketTest.test_ticket_invalid_user)

        db.session.commit()

        # Add the necessary objects
        db.session.add(BackEndBuyTicketTest.test_user)
        db.session.add(BackEndBuyTicketTest.test_user_2)
        db.session.add(BackEndBuyTicketTest.invalid_user)
        db.session.add(BackEndBuyTicketTest.test_ticket)
        db.session.add(BackEndBuyTicketTest.test_ticket_invalid_user)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        '''
        This gets run after all test cases in this class
        Use this method to remove any database changes you made.
        :return:
        '''

        # Remove it to restore original database
        # db.session.delete(test_user)
        db.session.delete(BackEndBuyTicketTest.test_user)
        db.session.delete(BackEndBuyTicketTest.test_user_2)
        db.session.delete(BackEndBuyTicketTest.invalid_user)
        db.session.delete(BackEndBuyTicketTest.test_ticket)
        db.session.delete(BackEndBuyTicketTest.test_ticket_invalid_user)
        db.session.commit()

    @classmethod
    def setUp(cls):
        # Reset certain database properties to make testing code simpler.

        BackEndBuyTicketTest.test_user.balance = 0
        BackEndBuyTicketTest.test_user_2.balance = 5000
        BackEndBuyTicketTest.test_ticket.quantity = 100
        db.session.commit()

    def test_valid_buy(self):
        '''
        Test case B1.1 (also tests B1.4, B1.6 and B1.8)
        This tests the ticket existing and a correct quantity to buy
        '''

        quantity = 2
        test_ticket = BackEndBuyTicketTest.test_ticket
        test_user_2 = BackEndBuyTicketTest.test_user_2
        owner = BackEndBuyTicketTest.test_user
        tickets_value = quantity*test_ticket.price + (quantity*test_ticket.price*0.4)

        self.assertTrue(bn.buy_ticket('t1', test_user_2, quantity))

        # Check changes to database took place

        # owner = User.query.filter_by(email=test_ticket.email).first()
        # buyer = User.query.filter_by(email=test_user_2.email).first()
        # ticket = Ticket.query.filter_by(name=test_ticket.name).first()
        self.assertTrue(owner.balance == quantity*test_ticket.price)
        self.assertTrue(test_user_2.balance == 5000 - tickets_value)
        self.assertTrue(test_ticket.quantity == 100 - quantity)

    def test_ticket_does_not_exist(self):
        '''
        Test case B1.2
        This tests when the ticket does not exist
        '''
        self.assertFalse(bn.buy_ticket('invalid', BackEndBuyTicketTest.test_user_2, 0))

    def test_ticket_invalid_quantity(self):
        '''
        Test case B1.3
        This tests when the user requests too many tickets
        '''
        self.assertFalse(bn.buy_ticket('t1', BackEndBuyTicketTest.test_user_2, 101))

    def test_insufficient_funds(self):
        '''
        Test case B1.5
        This tests when the user does not have the funds
        '''
        self.assertFalse(bn.buy_ticket('t1', BackEndBuyTicketTest.test_user_2, 72))

        # Verify no funds have been transferred or tickets
        self.assertTrue(BackEndBuyTicketTest.test_user.balance == 0)
        self.assertTrue(BackEndBuyTicketTest.test_user_2.balance == 5000)
        self.assertTrue(BackEndBuyTicketTest.test_ticket.quantity == 100)

    def test_database_integrity_fix(self):
        '''
        Test case B1.7
        This tests if the owner of the ticket does not have a balance the function fixes and doesn't crash
        '''

        quantity = 2
        tickets_value = quantity * BackEndBuyTicketTest.test_ticket_invalid_user.price
        self.assertTrue(bn.buy_ticket('t2', BackEndBuyTicketTest.test_user_2, quantity))

        # Make sure owner has gotten funds
        # user = User.query.filter_by(email=invalid_user.email).first()
        self.assertTrue(BackEndBuyTicketTest.invalid_user.balance == tickets_value)

