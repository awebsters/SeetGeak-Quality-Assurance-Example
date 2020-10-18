**R6 /buy **

**Test Case R6.1.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   Login with valid credentials

-   Open /buy

-   Click on 'input\[name="name"\]

-   Enter in invalid name

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The name of the ticket has to be alphanumeric-only, and space
    > allowed only if it is not the first or the last character'

**Test Case R6.2.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /buy

-   Click the name element input\[name="name"\]

-   Enter a name that has more than 60 characters

-   Enter valid information for the rest of the input fields

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that shows
    > 'Ticket name can be no longer than 60 characters\'

**Test Case R6.3.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /buy

-   Click on 'input\[name="quantity"\]

-   Enter in 0

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The quantity of the tickets has to be more than 0, and less than
    > or equal to 100

**Test Case R6.3.2**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /buy

-   Click on 'input\[name="quantity"\]

-   Enter in 101

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The quantity of the tickets has to be more than 0, and less than
    > or equal to 100

**Test Case R6.4.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /buy

-   Click on 'input\[name="name"\]

-   Enter an valid name

-   Click on 'input\[name="quantity"\]

-   Enter invalid quantity

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that shows
    > the quantity is not more than the quantity requested to buy

**Test Case R6.5.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /

-   Validate that the balance is 0

-   Open /buy

-   Enter in rest of valid credentials

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that the
    > user does not have more balance than the ticket price \*
    > quantity + service fee (35%) + tax (5%)

**Test Case R6.6.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   This can be validated cases R6.1.1 - R6.5.1

**R7 /logout**

**Test Case R7.1.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a None

Actions:

-   Logout

-   Try to access /sell

-   Verify you cannot access the page

-   Validate that you are redirected to /login

-   Try to access /buy

-   Verify you cannot access the page

-   Validate that you are redirected to /login

-   Try to access /update

-   Verify you cannot access the page

-   Validate that you are redirected to /login
