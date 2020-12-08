# Buy_Ticket Backend Testing

This function will be tested by a white box testing method, more specifically by a decision coverage.
This coverage type has been selected due to the high variety of conditions related to the code implementation for this function.

A simple analysis of the code yields the following possible condition table:

Note - The following User and ticket will be available in the database:


test_user = User(\
&nbsp;&nbsp; email='test_backend@test.com',\
&nbsp;&nbsp; name='test_backend',\
&nbsp;&nbsp; password=generate_password_hash('Test_frontend', method='sha256'),\
&nbsp;&nbsp; balance=0\
)

test_user_2 = User(\
&nbsp;&nbsp; email='test_backend@test.com',\
&nbsp;&nbsp; name='test_backend',\
&nbsp;&nbsp; password=generate_password_hash('Test_backend', method='sha256'),\
&nbsp;&nbsp; balance=5000\
)

invalid_user = User(\
&nbsp;&nbsp; email='test_invalid@test.com',\
&nbsp;&nbsp; name='test_invalid',\
&nbsp;&nbsp; password=generate_password_hash('Test_invalid', method='sha256'),\
)

test_ticket = Ticket(\
&nbsp;&nbsp; name: 't1',\
&nbsp;&nbsp; price: 50.0,\
&nbsp;&nbsp; quantity: 100,\
&nbsp;&nbsp; email: test_backend@test.com\
)

test_ticket_invalid_user = Ticket(\
&nbsp;&nbsp; name: 't2',\
&nbsp;&nbsp; price: 50.0,\
&nbsp;&nbsp; quantity: 100,\
&nbsp;&nbsp; email: test_invalid@test.com\
)

| Condition                                                          | True or False | Test Case ID | name input | user input | quantity input | Expected Return |
|--------------------------------------------------------------------|---------------|--------------|------------|------------|----------------|-----------------|
| ticket exists (get_ticket(name))                                   | True          | B1.1         | t1         | test_user_2  | 2              | 1               |
| ticket exists (get_ticket(name))                                   | False         | B1.2         | Invalid    | test_user_2  | 0              | 0               |
| ticket.quantity < quantity                                         | True          | B1.3         | t1         | test_user_2  | 101              | 0               |
| ticket.quantity < quantity                                         | False         | B1.4         | t1         | test_user_2  | 2              | 1               |
| user.balance < ticket.price*quantity + (ticket.price*quantity*0.4) | True          | B1.5         | t1         | test_user_2  | 72             | 0               |
| user.balance < ticket.price*quantity + (ticket.price*quantity*0.4) | False         | B1.6         | t1         | test_user_2  | 2              | 1               |
| not seller.balance                                                 | True          | B1.7         | t2         | test_user_2  | 2              | 1               |
| not seller.balance                                                 | False         | B1.8         | t1         | test_user_2  | 2              | 1               |

This provides a coverage of all conditions in the code. We notice test cases B1.4, B1.6 and B1.8 are all duplicates of other test cases.
Therefore, there cases can be removed when testing code is implemented.