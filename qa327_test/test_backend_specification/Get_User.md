# Get User Function

This function accepts an email address and returns a user object from the database

There are simply two partitions for this function.

1. A user exists in the database for that email address
   1. This should return the user object
2. A user does not exists in the database for that email address
   1. This should return None