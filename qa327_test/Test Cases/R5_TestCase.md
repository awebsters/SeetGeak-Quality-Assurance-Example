**R5 /update**

**Test Case R5.1.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="name"\]

-   Enter in invalid name

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate redirect to /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The name of the ticket has to be alphanumeric-only, and space
    > allowed only if it is not the first or the last character'

**Test Case R5.2.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="quantity"\]

-   Enter a name that contains greater than 60 characters

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate redirect to /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The name of the ticket is no longer than 60 characters

**Test Case R5.3.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="quantity"\]

-   Enter in 0

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate redirect to /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The quantity of the tickets has to be more than 0, and less than
    > or equal to 100

**Test Case R5.3.2**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="quantity"\]

-   Enter in number greater than a 100

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate redirect to /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The quantity of the tickets has to be more than 0, and less than
    > or equal to 100

**Test Case R5.4.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click the name element input\[name="price"\]

-   Enter a price that is under 10

-   Enter valid information for the rest of the input fields

-   Click on 'input\[name="submit"\]

-   Validate redirect /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'Ticket price cannot be less than 10 dollars\'

**Test Case R5.4.2**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click the name element input\[name="price"\]

-   Enter a price that is over 100

-   Enter valid information for the rest of the input fields

-   Click on 'input\[name="submit"\]

-   Validate redirect to /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'Ticket price cannot be more than 100 dollars\'

**Test Case R5.5.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="Date"\]

-   Enter in wrong format

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Redirect to /

-   Validate that current page contains\`\#error\_message\` that shows
    > 'Date must be given in the format YYYYMMDD (e.g. 20200901)

**Test Case R5.5.2**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="Date"\]

-   Enter in correct format

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate redirect to /

-   Validate that current page does not contains\`\#error\_message\`
    > that shows 'Date must be given in the format YYYYMMDD
    > (e.g. 20200901)

**Test Case R5.6.1**

Test Data:

None

Mocking:

-   Mock backend.get\_user to return a test\_user instance

-   Mock backend.get\_all\_tickets to return a test\_tickets instance

Actions:

-   open /logout (to invalidate any logged-in sessions that may exist)

-   Login with valid credentials

-   Open /update

-   Click on 'input\[name="name"\]

-   Enter invalid ticket name

-   Enter in rest of credentials

-   Click on 'input\[name="submit"\]

-   Validate that current page contains\`\#error\_message\` that shows
    > 'The ticket of the given name must exist

**Test Case R5.7.1**

Actions:

-   This is tested with R5.1.1-R5.6.1
