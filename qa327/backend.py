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
        new_user = User(email=email, name=name, password=hashed_pw, balance=1000)

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

#Backend functionality for ticket buying
def buy_ticket(name, user, quantity):
    #Make sure ticket exists
    if (get_ticket(name)):
        ticket = get_ticket(name)
        #Make sure enough quantity of tickets exist and user has enough balance
        if ticket.quantity < quantity:
            return 0
        elif (user.balance < (ticket.price*quantity + (ticket.price*quantity*0.4))):
            return 0
        else:
            #Subtracts the ticket amount plus services and tax from the buyers account
            user.balance -= quantity*ticket.price + (quantity*ticket.price*0.4)
            #Gets the seller's user data
            seller = get_user(ticket.email)
            #Set the seller's balance to 0 if the seller's balance is set to None to avoid a crash
            if not seller.balance:
                seller.balance = 0
            #Add the ticket sale revenue to the sellers balance
            seller.balance += quantity*ticket.price
            #Check if there are still tickets left after the order is complete
            if (ticket.quantity > quantity):
                #If there are tickets left, subtract the amount bought from the total available tickets
                ticket.quantity -= quantity
            else:
                #if not, delete the ticket from the database
                db.session.delete(ticket)
            #commit all changes to the database
            db.session.commit()
    else:
        return 0 
    return 1  
