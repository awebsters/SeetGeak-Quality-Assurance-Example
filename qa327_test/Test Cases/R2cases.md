**R2 /register**

**Test Case R2.1.1**

Test Data:

test_user = User(

    email='test_frontend@test.com',

    name='test_frontend',

    password=generate_password_hash('test_frontend')

)

Mocking:

● Mock backend.get_user to return a test_user instance

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter test_user's email into element #email

● enter test_user's password into element #password

● click element input[type="submit"]

● Open /register

● Validate that it has redirected to the / page

**Test Case R2.2.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● Open /register

● Validate that the /register page doesn't redirect

**Test Case R2.3.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /register

● Validate 'input[name="email]' exists and can take input

● Validate 'input[type="password"]' exists and can take input

● Validate 'input[type="password2"]' exists and can take input

● Validate 'input[name="name"]' exists and can take input

**Test Case R2.4.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open `base_url + /register

● validate that current page contains `please register` in element `#message`

**Test Case R2.5.1**

Test Data:

None

Mocking:

● Mock backend.get_user to return a None

● Mock backend.register_user to return a None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /register

● click element `input[name="email"]`

● Enter a valid email

● click element `input[name="password"]`

● Enter valid password

● click element `input[name="password2"]`

● Enter same input as for `input[name="password"]`

● click element `input[name="name"]`

● Enter a valid username

● click element `input[type="submit"]`

● Validate the user is redirected to /login

**Test Case R2.5.2**

Actions:

● Duplicate R2.5.1 with the following changes:

○ Change to invalid email entered into 'input[name='email']'

○ Instead of redirection validation: validate that current page contains`#error_message` that shows `email has to be an actual email address'

**Test Case R2.5.3**

Actions:

● Duplicate R2.5.1 with the following changes:

○ Change to invalid password entered into 'input[name='password']' by making the length < 6

○ Instead of redirection validation: validate that current page contains`#error_message` that shows `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character'

**Test Case R2.5.4**

Actions:

● Duplicate R2.5.1 with the following changes:

○ Change to invalid password entered into 'input[name='password']' by removing all uppercase letters

○ Instead of redirection validation: validate that current page contains`#error_message` that shows `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character'

**Test Case R2.5.5**

Actions:

● Duplicate R2.5.1 with the following changes:

○ Change to invalid password entered into 'input[name='password']' by removing all lowercase letters

○ Instead of redirection validation: validate that current page contains`#error_message` that shows `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character'

**Test Case R2.5.6**

Actions:

● Duplicate R2.5.1 with the following changes:

○ Change to invalid password entered into 'input[name='password']' by removing all special characters

○ Instead of redirection validation: validate that current page contains`#error_message` that shows `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character'

**Test Case R2.6**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● Open /register

● Click  'input[type="password"]' and enter '12345'

● Click  'input[type="password2"]' and enter '123456'

● Click  'input[name="email"]' and enter a valid email

● Click  'input[name="email"]' and enter a valid username

● Click  'input[name="name"]' and enter a valid name

● Click  'input[name="submit"]

● validate that current page contains`#error_message` that shows 'The passwords do not match'

**Test Case R2.7.1**

Test Data:

None

Mocking:

● Mock backend.get_user to return a None

● Mock backend.register_user to return a None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● Open /register

● click element `input[name="email"]`

● Enter an valid email

● click element `input[name="password"]`

● Enter valid password

● click element `input[name="password2"]`

● Enter password matching 'input[name='password']'

● Click  'input[name="submit"]

● Validate that current page contains`#error_message` that shows 'User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character'

**Test Case R2.7.2**

Test Data:

None

Mocking:

● Mock backend.get_user to return a None

● Mock backend.register_user to return a None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● Open /register

● click element `input[name="email"]`

● Enter an valid email

● click element `input[name="name"]`

● Enter an invalid username (username contains non-alphanumeric)

● click element `input[name="password"]`

● Enter valid password

● click element `input[name="password2"]`

● Enter password matching 'input[name='password']'

● Click  'input[name="submit"]

● Validate that current page contains`#error_message` that shows 'User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character'

**Test Case R2.7.3**

Actions:

● Duplicate R2.7.2 with the following change

○ Enter a valid email address and add a space to the start (to make it invalid)

**Test Case R2.7.4**

Actions:

● Duplicate R2.7.2 with the following change

○ Enter a valid email address and add a space to the end (to make it invalid)

**Test Case R2.8.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /register

● click element `input[name="email"]`

● Enter a valid email

● click element `input[name="password"]`

● Enter valid password

● click element `input[name="password2"]`

● Enter same input as for `input[name="password"]`

● click element `input[name="name"]`

● Enter a username of length 2

● click element `input[type="submit"]`

● Validate that current page contains`#error_message` that shows 'Username has to be longer than 2 characters and less than 20 characters.'

**Test Case R2.8.2**

Actions:

● Duplicate of R2.8.1 with the following change

○ Make username of length 20

**Test Case R2.9.1**

Actions:

● Test R2.5.1-R2.8.3 can validate this requirement

**Test Case R2.10.1**

Test Data:

test_user = User(

    email='test_frontend@test.com',

    name='test_frontend',

    password=generate_password_hash('test_frontend')

)

Mocking:

● Mock backend.get_user to return a test_user instance

● Mock backend.register_user to return None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /register

● click element `input[name="email"]`

● Enter a test_users email

● click element `input[name="password"]`

● Enter valid password

● click element `input[name="password2"]`

● Enter same input as for `input[name="password"]`

● click element `input[name="name"]`

● Enter a username of length 2

● click element `input[type="submit"]`

● Validate that current page contains`#error_message` that shows 'this email has been ALREADY used.'

**Test Case R2.11.1**

Test Data:

None

Mocking:

● Mock backend.get_user to return a User Instance

● Mock backend.register_user to return a None

● Mock backend.set_balance to return None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /register

● enter credentials

● Click on  'input[name="submit"]

● Open /balance

● Click on  'input[name="balance"]

● Enter 5000

● Click on  'input[name="submit"]

● open /

● Verify Balance is set to 5000

● open /logout (to invalidate any logged-in sessions that may exist)

● Open logout