from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """
    try:
        hashed_pw = generate_password_hash(password, method='sha256')
        # store the encrypted password rather than the plain password
        new_user = User(email=email, name=name, password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()
    except:
        return False
            
    return True


def get_all_tickets():
    return Ticket.query.all()


def get_ticket(name):
    ticket = Ticket.query.filter_by(name=name).first()
    return ticket


def create_ticket(name, quantity, price, date, email):
    new_ticket = Ticket(name=name, quantity=quantity,
                        price=price, date=date, email=email)
    db.session.add(new_ticket)
    db.session.commit()
    return None


def update_ticket(name, quantity, price, date):
    ticket = get_ticket(name)

    #Check that ticket exists
    if ticket is None:
        return 0
    else:
        ticket.quantity = quantity
        ticket.price = price
        ticket.date = date
        db.session.update(ticket)
        db.session.commit()
    return 1

