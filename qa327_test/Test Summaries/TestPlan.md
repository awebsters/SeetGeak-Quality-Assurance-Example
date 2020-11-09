-   How test cases of different levels (frontend, backend units,
    > integration) are organized.

They are organized into different folders, with their own test scripts.
All the folders are located in the test directory. Front end, back end
and integration unit tests will each have their own folders and each
requirement R1-R8 will have it's own testing script inside each folder.

-   The order of the test cases (which level first which level second).

The order of our test cases will be as follows; Backend unit tests
first, Front end unit tests second and then integration tests last. We
will be doing backend unit tests first as this is a critical section
that must be functioning perfectly for the application to function
correctly. Next we do front end testing as the user\'s interaction with
the application needs to be functioning as expected or our application
becomes unusable. Lastly we test Integration, however, we place a key
importance on this step cannot be "left behind". We test this last as
this application does not contain a complex integration, therefore
making the other sections of higher priority

Backend units: 1st

Frontend: 2nd

Integration: 3rd

-   Techniques and tools used for testing.

The main tools we will use for our testing are Github actions, Pytest
and Selenium. Pytest is a testing framework which allows us to write
test codes using python, and will be utilized in all of our test cases.
Github actions will be used to run our tests on the repository. Finally
Selenium is a testing framework that automates browser actions, allowing
us to test the front end of our application. In terms of techniques, we
will create unit tests for every possible test case and then create
integration tests to test how all parts of our application interact.

Tools: Github Actions, Pytest, Selenium

Selenium webdriver is used to test the frontend

Github Actions is used to run tests on repo

Pytest is a testing framework which allows us to write test codes using
python

Unit tests for every specification

-   Environemnts (all the local environment and the cloud environment)
    > for the testing.

Using Github Actions, tests will be used for merge requests. For local
environments, devs can run the test scripts themselves from the
organized folders.

-   Responsibility (who is responsible for which test case, and in case
    > of failure, who should you contact)

R1 /login - Max

R2 /register - Hatim

R3 / - Alex

R4 /sell - Hatim

R5 /update - Cathy

R6 /buy - Alex

R7 /logout - Max

R8 /\* - Max

In the case of failure contact the tester for that route. For example,
if a failure is found in /login contact Max.

-   Budget Management (you have limited CI action minutes, how to
    > monitor, keep track and minimize unncessary cost)

We only run CI action for vital tests. We also don't send it to test
until every member has submitted a code review, and issues have been
resolved on merge requests. We will keep track of our CI action minutes
used in a common document to make sure we budget our time effectively.
By keeping track we can adjust this strategy according to resources left
relative to the remaining project timeline. In addition, our method of
testing on merge requests is effective as individuals can run tests
locally to save these resources (using the levels method to do full
testing locally as the testing suite gets larger). It is only required
to run the full accepted master testing suite when merging to master as
a final check to make sure master contains the highest quality code.
