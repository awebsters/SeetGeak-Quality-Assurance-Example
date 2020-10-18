{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 **R6 /buy **\
\
**Test Case R6.1.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   Login with valid credentials\
\
-   Open /buy\
\
-   Click on 'input\\[name="name"\\]\
\
-   Enter in invalid name\
\
-   Enter in rest of credentials\
\
-   Click on 'input\\[name="submit"\\]\
\
-   Validate that current page contains\\`\\#error\\_message\\` that shows\
    > 'The name of the ticket has to be alphanumeric-only, and space\
    > allowed only if it is not the first or the last character'\
\
**Test Case R6.2.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   open /logout (to invalidate any logged-in sessions that may exist)\
\
-   Login with valid credentials\
\
-   Open /buy\
\
-   Click the name element input\\[name="name"\\]\
\
-   Enter a name that has more than 60 characters\
\
-   Enter valid information for the rest of the input fields\
\
-   Click on 'input\\[name="submit"\\]\
\
-   Validate that current page contains\\`\\#error\\_message\\` that shows\
    > 'Ticket name can be no longer than 60 characters\\'\
\
**Test Case R6.3.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   open /logout (to invalidate any logged-in sessions that may exist)\
\
-   Login with valid credentials\
\
-   Open /buy\
\
-   Click on 'input\\[name="quantity"\\]\
\
-   Enter in 0\
\
-   Enter in rest of credentials\
\
-   Click on 'input\\[name="submit"\\]\
\
-   Validate that current page contains\\`\\#error\\_message\\` that shows\
    > 'The quantity of the tickets has to be more than 0, and less than\
    > or equal to 100\
\
**Test Case R6.3.2**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   open /logout (to invalidate any logged-in sessions that may exist)\
\
-   Login with valid credentials\
\
-   Open /buy\
\
-   Click on 'input\\[name="quantity"\\]\
\
-   Enter in 101\
\
-   Enter in rest of credentials\
\
-   Click on 'input\\[name="submit"\\]\
\
-   Validate that current page contains\\`\\#error\\_message\\` that shows\
    > 'The quantity of the tickets has to be more than 0, and less than\
    > or equal to 100\
\
**Test Case R6.4.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   open /logout (to invalidate any logged-in sessions that may exist)\
\
-   Login with valid credentials\
\
-   Open /buy\
\
-   Click on 'input\\[name="name"\\]\
\
-   Enter an valid name\
\
-   Click on 'input\\[name="quantity"\\]\
\
-   Enter invalid quantity\
\
-   Enter in rest of credentials\
\
-   Click on 'input\\[name="submit"\\]\
\
-   Validate that current page contains\\`\\#error\\_message\\` that shows\
    > the quantity is not more than the quantity requested to buy\
\
**Test Case R6.5.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   open /logout (to invalidate any logged-in sessions that may exist)\
\
-   Login with valid credentials\
\
-   Open /\
\
-   Validate that the balance is 0\
\
-   Open /buy\
\
-   Enter in rest of valid credentials\
\
-   Click on 'input\\[name="submit"\\]\
\
-   Validate that current page contains\\`\\#error\\_message\\` that the\
    > user does not have more balance than the ticket price \\*\
    > quantity + service fee (35%) + tax (5%)\
\
**Test Case R6.6.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a test\\_user instance\
\
-   Mock backend.get\\_all\\_tickets to return a test\\_tickets instance\
\
Actions:\
\
-   This can be validated cases R6.1.1 - R6.5.1\
\
**R7 /logout**\
\
**Test Case R7.1.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   Mock backend.get\\_user to return a None\
\
Actions:\
\
-   Logout\
\
-   Try to access /sell\
\
-   Verify you cannot access the page\
\
-   Validate that you are redirected to /login\
\
-   Try to access /buy\
\
-   Verify you cannot access the page\
\
-   Validate that you are redirected to /login\
\
-   Try to access /update\
\
-   Verify you cannot access the page\
\
-   Validate that you are redirected to /login\
\
**R8 /\\***\
\
**Test Case R8.1.1**\
\
Test Data:\
\
None\
\
Mocking:\
\
-   None\
\
Actions:\
\
-   Try to request /test\
\
-   Verify that you receive a 404 error\
\
Test Plan\
\
1.  \
\
We each created test cases and put them in separate mark down tables and\
then created separate PR's. Once all the markdown tables were merged\
onto github they were combined into one.\
\
2.  Your understanding of how the chosen testing framework works to test\
    > the frontend, including your understandings of when and how the\
    > test cases will be running directly on GitHub.\
\
We'll be using Selenium to automate the front-end testing. When the\
Selenium script runs the front-end will be sending requests to a mock\
API that returns test data.\
\
These tests will run when there is a PR on Github to make sure the PR\
doesn't break anything.\
\
How are you going to organize different test case code files? (a folder\
for a specification?)\
\
We'll create a folder for all the test case files and subfolders for all\
the routes.\
}