R1 - /login

**Test Case R1.1.1**

Test Data:

            None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● Validate the current page is /login (no redirects have taken pace)

**Test Case R1.2.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● validate that current page has `please login` in element `#message`

**Test Case R1.3.1**

Test Data:

test_user = User(

    email='test_frontend@test.com',

    name='test_frontend',

    password=generate_password_hash('test_frontend'),

    Balance = 5000

)

Mocking:

● Mock backend.get_user to return a test_user instance

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter test_user's email into element #email

● enter test_user's password into element #password

● click element input[type="submit"]

● open /login again

● validate that current page contains #welcome-header element

**Test Case R1.4.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● validate that current page has element `#email`

● validate that current page has element `#password`

**Test Case R1.5.1**

Test Data:

test_user from previous test case

Mocking:

● Mock backend.get_user to return a test_user instance

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter test_user's email into element #email

● enter test_user's password into element #password

● click element input[type="submit"]

● Validate that the current page is the / page

**Test Case R1.6.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● Enter a password into element #password

● click element `input[type="submit"]`

● validate that current page contains`#error_message` that shows 'email/password format is incorrect.'

**Test Case R1.6.2**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● Enter an email into element #email

● click element `input[type="submit"]`

● validate that current page contains`#error_message` that shows 'email/password format is incorrect.'

**Test Case R1.6.3**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● click element `input[type="submit"]`

● validate that current page contains`#error_message` that shows 'email/password format is incorrect.'

**Test Case R1.7.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● Enter a valid syntax email to element #email

● Enter in a valid syntax password to element #password

● Click element 'input[type="submit"]'

● Validate that the current page does not contain 'email/password format is incorrect.' in the #error_message element

**Test Case R1.7.2**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● Enter an invalid syntax email to element #email

● Enter in a valid syntax password to element #password

● Click element 'input[type="submit"]'

● Validate that the current page does contain 'email/password format is incorrect.' in the #error_message element

**Test Case R1.8.1**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter a valid syntax email into element #email

● enter valid syntax password into element #password.

● Validate that the current page does not contain `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character' in the #error_message element

**Test Case R1.8.2**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter a valid syntax email into element #email

● enter valid syntax password except length < 6 into element #password.

● Validate that the current page does contain `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character' in the #error_message element

**Test Case R1.8.3**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter a valid syntax email into element #email

● enter valid syntax password except no uppercase character into element #password.

● Validate that the current page does contain `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character' in the #error_message element

**Test Case R1.8.4**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter a valid syntax email into element #email

● enter valid syntax password except no lowercase characters into element #password.

● Validate that the current page does contain `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character' in the #error_message element

**Test Case R1.8.5**

Test Data:

None

Mocking:

● None

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter a valid syntax email into element #email

● enter valid syntax password except no special characters into element #password.

● Validate that the current page does contain `Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character' in the #error_message element

**Test Case R1.9.1**

Test Data:

None

Mocking:

● None

Actions:

● Running test cases R1.7.1 - R1.8.5 without error will verify this specification

**Test Case R1.10.1**

Test Data:

test_user data from above

Mocking:

● Mock backend.get_user to return a test_user instance

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter test_user's email into element #email

● enter test_user's password into element #password

● click element input[type="submit"]

● Validate that the current page is the / page

**Test Case R1.11.1**

Test Data:

test_user data from above

Mocking:

● Mock backend.get_user to return a test_user instance

Actions:

● open /logout (to invalidate any logged-in sessions that may exist)

● open /login

● enter email that's not test_user  into element #email

● enter password that's not test_users into element #password

● click element input[type="submit"]

● Validate that the element #error_message contains 'email/password combination incorrect'

