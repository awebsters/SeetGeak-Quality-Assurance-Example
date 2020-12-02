from flask import render_template, request, session, redirect
from qa327 import app
import re
import qa327.backend as bn
import re
from datetime import datetime

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder.
"""

@app.route('/register', methods=['GET'])
def register_get():
    if 'logged_in' in session:
        return redirect('/')
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
        
    patternEmail = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    patternPass = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[^A-Za-z0-9]).{6,}$")

    patternName = re.compile(r"^\w[\w ]+\w$")

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
        session['error'] = error_message
        return redirect('/login')
    elif not patternEmail.fullmatch(email):
        error_message =  '{} format is incorrect.'.format("Email")
        session['error'] = error_message
        return redirect('/login')

    elif not patternPass.fullmatch(password):
        error_message =  '{} format is incorrect.'.format("Password")
        session['error'] = error_message
        return redirect('/login')

    elif not patternName.fullmatch(name) or len(name) < 2 or len(name) > 20:
        error_message =  '{} format is incorrect.'.format("Name")
        session['error'] = error_message
        return redirect('/login')

    user = bn.get_user(email)
    if user:
        error_message = "This email has been ALREADY used"
    elif not bn.register_user(email, name, password, password2):
        error_message = "Failed to store user info."

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    if 'logged_in' in session:
        return redirect('/')
    message = 'Please login'
    if "error" in session:
        message = session["error"]
        del session["error"]

    return render_template('login.html', message=message)


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    #regex for email obtained from https://emailregex.com/
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    PASSWORD_REGEX = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[^A-Za-z0-9]).{6,}$")
    if  not EMAIL_REGEX.match(email) or not PASSWORD_REGEX.match(password):
        return render_template('login.html', message='email/password format invalid')
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information
        between browser and the end server. Typically it is encrypted
        and stored in the browser cookies. They will be past
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='email/password combination incorrect')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def check_ticket_form(name=None, quantity=None, price=None, date=None):
    '''
    Will check for valid form entries for name, quantity, price, and date of a ticket form.
    Will not validate a parameter if its value is passed in as None
    :return: An error message string or None if no error found
    '''
    if name:
        if name[0] == ' ' or name[len(name) - 1] == ' ':
            return "Name has space at beginning or end"
        elif not name.isalnum():
            return "Name can only contain alphanumeric characters"
        elif len(name) > 60:
            return "Name is too long, it must be shorter than 60 characters"
    if quantity:
        if not quantity.isnumeric():
            return "Quantity must be a number"
        elif int(quantity) < 0 or int(quantity) > 100:
            return "Quantity must be greater than 0 and less than or equal to 100"
    if price:
        try:
            float(price)
        except ValueError:
            return "Price must be a number"
        if float(price) < 10 or float(price) > 100:
            return "Price must be greater than or equal to 10 and less than or equal to 100"
    if date:
        if not datetime.strptime(date, "%Y-%m-%d"):
            return "Date must be in the format YYYY-MM-DD"


@app.route('/sell', methods=['POST'])
def sell():
    """
    Route to sell a new ticket. 
    This route will validate the ticket form, if valid it will use a backend function
    to commit to the database  
    """
    if 'logged_in' not in session:
        return redirect('/login')

    name = request.form.get('name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    date = request.form.get('date')

    error_message = check_ticket_form(name, quantity, price, date)
    tickets = bn.get_all_tickets()
    user = bn.get_user(session['logged_in'])
    if error_message:
        return render_template('index.html', sell_message=error_message, tickets=tickets, user=user)

    bn.create_ticket(name, quantity, price, date, user.email)
    return redirect('/', code=303)


@app.route('/buy', methods=['POST'])
def buy():
    """
    Route to buy a ticket.
    This route will validate the ticket form, if valid it will update the database
    through a backend function
    """
    if 'logged_in' not in session:
        return redirect('/login')
    email = session['logged_in']
    #Get user information
    user = bn.get_user(email)
    #Sets the error message to blank initially
    error_message=""
    #Get information from the form
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    #Get all tickets to pass to backend function
    tickets = bn.get_all_tickets()
    #Checks to make sure name and quantity form values are valid, sends error if they are invalid 
    if (len(name) > 60):
        error_message = "Name is too long, it must be shorter than 60 characters"
    elif(name[0] == ' ' or name[len(name) - 1] == ' '):
        error_message = "Name has space at beginning or end"
    elif not (name.isalnum()):
        error_message = "Name can only contain alphanumeric characters"
    elif not (quantity.isnumeric()):
        error_message = "Quantity must be a number"
    elif(int(quantity) < 0 or int(quantity) > 100):
        error_message = "Quantity must be greater than 0 and less than or equal to 100"
    elif (bn.buy_ticket(name,user,int(quantity))):
        message = "Tickets bought succesfully"
    else:
        error_message = "Ticket could not be bought"
    #Checks if there is an error, and if there is set the error message 
    if len(error_message) > 0:
        session['error'] = error_message
        message = session["error"]
        del session["error"]
    return render_template('index.html', buy_message=message, user=user, tickets=tickets)

def displayUpdateMessage(message):
    return render_template('index.html', update_message=message)
  
@app.route('/update', methods=['POST'])
def update():
    """
    Route to update a ticket.
    This route will validate the ticket form, if valid it will update the ticket on the database
    through a backend function
    """
    if 'logged_in' not in session:
        return redirect('/login')

    #Grab necessary information from update form
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    date = request.form.get('date')

    #Check if name is valid
    if (len(name) > 60):
        return displayUpdateMessage('Name is too long')

    if (name[0] == ' ' or name[len(name) - 1] == ' '):
        return displayUpdateMessage('Name has space at beginning or end')

    if not (name.isalnum()):
        return displayUpdateMessage('Name can only be alphanumeric')

    #Check if ticket exists in database
    ticket = bn.get_ticket(name)
    if (ticket is None):
        return displayUpdateMessage('Ticket does not exist')

    #Check if quantity is valid
    if not (quantity.isnumeric()):
        return displayUpdateMessage('Quantity must be a number')

    if (int(quantity) < 0 or int(quantity) > 100):
        return displayUpdateMessage('Quantity must be greater than 0 and less than 100')

    #Check if price is valid
    if not (price.isnumeric()):
        return displayUpdateMessage('Price must be a number')

    if (price < 10 or price > 100):
        return displayUpdateMessage('Price has to be in range between 10 to 100')

    #Check if date is valid
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return displayUpdateMessage('Date must be given in format YYYYMMDD')

    #Update tickets to database
    bn.update_ticket(name, quantity, price, date)
    return displayUpdateMessage('Successfully updated tickets')


