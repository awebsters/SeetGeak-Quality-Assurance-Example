**R8 /\***

**Test Case R8.1.1**

Test Data:

None

Mocking:

-   None

Actions:

-   Try to request /test

-   Verify that you receive a 404 error

Test Plan

1.  

We each created test cases and put them in separate mark down tables and
then created separate PR's. Once all the markdown tables were merged
onto github they were combined into one.

2.  Your understanding of how the chosen testing framework works to test
    > the frontend, including your understandings of when and how the
    > test cases will be running directly on GitHub.

We'll be using Selenium to automate the front-end testing. When the
Selenium script runs the front-end will be sending requests to a mock
API that returns test data.

These tests will run when there is a PR on Github to make sure the PR
doesn't break anything.

How are you going to organize different test case code files? (a folder
for a specification?)

We'll create a folder for all the test case files and subfolders for all
the routes.
