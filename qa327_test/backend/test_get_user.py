from unittest.mock import patch
from unittest import TestCase
from qa327.models import db, User
import qa327.backend as bn
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='test_backend@test.com',
    name='test_backend',
    password=generate_password_hash('Test_frontend', method='sha256'),
    balance=5000
)


class BackEndGetUserTest(TestCase):

    SHOULD_REMOVE = True
    @classmethod
    def setUpClass(cls):
        '''
        This gets run before all test cases in this class
        Use this method to make any database changes you need before running the
        backend code
        '''

        # Should only add to the database if it doesn't already exist
        if User.query.filter_by(email=test_user.email).first():
            BackEndGetUserTest.SHOULD_REMOVE = False
        else:
            db.session.add(test_user)
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        '''
        This gets run after all test cases in this class
        Use this method to remove any database changes you made.
        :return:
        '''

        # If didn't already exist, remove it to restore original database
        if BackEndGetUserTest.SHOULD_REMOVE:
            db.session.delete(test_user)
            db.session.commit()

    def test_email_not_exists(self):
        '''
        Make sure get_user returns None if the user doesn't exist
        '''

        # Give an impossible email to be in the database from frontend testing
        self.assertIsNone(bn.get_user(test_user.email + '1'))

    def test_email_exists(self):
        self.assertIsNotNone(bn.get_user(test_user.email))
